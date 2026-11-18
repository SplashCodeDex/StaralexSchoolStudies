"""One-shot harvest session runner (dork discovery -> sitemap harvest -> report).

Focuses on the knowlede gaps flagged by the tutor loop:
  * Computing/ICT: real BECE 2023-2025 papers, 2026 school mocks & marking schemes
  * CDT/CAD (Career Technology / Creative Arts & Design, Pre-Technical Skills):
    anything after 2022, 2026 mocks
  * General mock papers (classified in queue)

Deduplication is enforced by DownloadPipeline (is_url_visited + SHA-256
is_content_known + reject ledger), so re-running this session is idempotent.

Usage:
    python src/harvest_session.py --dorks-only          # fast dork phase only
    python src/harvest_session.py --max-articles 80     # full session, capped article crawl
    python src/harvest_session.py --report-only         # print session stats, do not crawl
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.config import DATABASE_PATH
from src.database import CatalogDatabase
from src.download_pipeline import DownloadPipeline
from src.dorker import DorkDiscoveryEngine
from src.sitemap_harvester import SitemapHarvester

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger("HarvestSession")

# 2026-season and CAD/ICT gap-filling queries (dedup at pipeline level is idempotent)
SESSION_QUERIES = [
    # Computing / ICT multi-year + 2026 season
    'filetype:pdf "BECE" "ICT" "past questions" ghana',
    'filetype:pdf "BECE" "computing" "2018" OR "2019" OR "2020" OR "2021" OR "2022" OR "2023"',
    'filetype:pdf "BECE" "computing" "Paper 1" "Paper 2" answers',
    'filetype:pdf "BECE" "2026" ("computing" OR "ICT") (mock OR "super mock" OR "serial mock")',
    'filetype:pdf "2026" BECE "marking scheme" ("computing" OR "ICT")',
    'filetype:pdf "2026 mock" ("computing" OR "ICT") ghana junior high',
    'filetype:pdf ("computing" OR "ICT") "mock 1" OR "mock 2" "2026" BECE ghana',
    # CDT / CAD / Pre-tech / Career Technology after 2022 + 2026 season
    'filetype:pdf "BECE" "pre-technical skills" OR "pre technical" past questions',
    'filetype:pdf "BECE" "career technology" mock 2020 OR 2021 OR 2022 OR 2023 OR 2024',
    'filetype:pdf "BECE" "2026" ("career technology" OR "pre-technical" OR "CAD") mock questions',
    'filetype:pdf "2026 mock" ("career technology" OR "creative arts and design") ghana',
    'filetype:pdf "home economics" "BECE" past questions ghana',
    'filetype:pdf "BECE" "creative arts" mock questions ghana',
    # Generic 2026 mock season sweep (classifier will auto-sort subjects)
    'filetype:pdf "BECE" "first mock" OR "second mock" OR "third mock" 2026',
    'filetype:pdf "2026" BECE mock "marking scheme" ghana',
    'site:becezone.com 2026 filetype:pdf',
    'site:ghanaeducation.org 2026 mock (filetype:pdf OR filetype:docx)',
]


async def run_dork_phase(custom_queries: list[str]) -> tuple[int, int, int]:
    """Dork discovery + direct downloads. Returns (new_downloads, already_known, rejected_count_before)."""
    db = CatalogDatabase()
    before = _count(db)

    engine = DorkDiscoveryEngine()
    logger.info("Running %d dork queries...", len(custom_queries))
    results = await engine.run_discovery(custom_queries=custom_queries)
    direct = DorkDiscoveryEngine.filter_direct_files(results)
    logger.info("Dork discovery: %d hits, %d direct-file candidates.", len(results), len(direct))

    pipeline = DownloadPipeline(database=db)
    new_downloads = 0
    for r in direct:
        res = await pipeline.download_file(url=r["url"], context_text=r.get("title", ""))
        if res:
            new_downloads += 1
            logger.info("NEW: %s", res[0].name)
        else:
            logger.info("skip (dup/visited/reject): %s", r["url"][:110])

    after = _count(db)
    db.export_catalog_json()
    stats = (after["total"] - before["total"], after["total"], after["by_subject"])
    return stats


async def run_sitemap_phase(max_articles: int) -> int:
    """Sitemap bulk harvest across all configured target sites."""
    harvester = SitemapHarvester()
    return await harvester.harvest(max_articles=max_articles)


def _count(db: CatalogDatabase) -> dict:
    with sqlite3.connect(db.db_path) as conn:
        total = conn.execute("SELECT COUNT(*) FROM harvested_files;").fetchone()[0]
        by_subject = {
            row[0]: row[1]
            for row in conn.execute(
                "SELECT subject, COUNT(*) FROM harvested_files GROUP BY subject;"
            ).fetchall()
        }
    return {"total": total, "by_subject": by_subject}


async def main() -> int:
    ap = argparse.ArgumentParser(description="Run a focused BECE paper harvest session")
    ap.add_argument("--dorks-only", action="store_true", help="Skip sitemap crawl phase")
    ap.add_argument("--dorks-off", action="store_true", help="Skip dork phase (sitemap only)")
    ap.add_argument("--max-articles", type=int, default=120, help="Max articles to open in sitemap phase")
    ap.add_argument("--report-only", action="store_true", help="Print bank stats and exit")
    ap.add_argument("--json", action="store_true", help="Machine-readable report")
    args = ap.parse_args()

    db = CatalogDatabase()
    if args.report_only:
        print(json.dumps(_count(db), indent=2))
        return 0

    if not args.dorks_off:
        (added, total, by_subject) = (await run_dork_phase(SESSION_QUERIES))
        logger.info("Dork phase complete: %d new papers (bank total now %d).", added, total)
        logger.info("By subject: %s", json.dumps(by_subject))

    if not args.dorks_only:
        n = await run_sitemap_phase(max_articles=args.max_articles)
        logger.info("Sitemap phase complete: %d new papers.", n)

    print(json.dumps({"final_state": _count(db)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
