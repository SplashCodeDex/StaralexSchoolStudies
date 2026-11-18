"""Manual URL list download through the dedup pipeline (Coleman 2026 BECE batch + misc)."""

import asyncio
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.download_pipeline import DownloadPipeline
from src.database import CatalogDatabase

URLS = [
    # 2026 BECE question papers (Coleman Publications)
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Computing-1-2.pdf", "2026 BECE Computing Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Career-Technology-1-2.pdf", "2026 BECE Career Technology Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Creative-Arts-and-Design-1-2.pdf", "2026 BECE Creative Arts and Design Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Core-Mathematics-1-2.pdf", "2026 BECE Core Mathematics Paper 1 and 2"),
    # 2026 BECE marking schemes
    ("https://colemanpublications.com/wp-content/uploads/2026/05/BECE-2026-COMPUTING-MARKING.pdf", "2026 BECE Computing Marking Scheme"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-MATHEMATICS-MARKING-SCHEME.pdf", "2026 BECE Mathematics Marking Scheme"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Performing-Arts-Marking-Scheme.pdf", "2026 BECE Performing Arts Marking Scheme"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/RME-BECE-2026-MARKING-SCHEME.pdf", "2026 BECE RME Marking Scheme"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/BECE-2026-ENGLISH-MARKING-SCHEME.pdf", "2026 BECE English Marking Scheme"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Social-Studies-Marking-Scheme.pdf", "2026 BECE Social Studies Marking Scheme"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-INTEGRATED-SCIENCE-MARKING-Scheme.pdf", "2026 BECE Integrated Science Marking Scheme"),
    # 2026 BECE remaining question papers (coverage completeness)
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-English-Language-1-2.pdf", "2026 BECE English Language Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Integrated-Science-1-2.pdf", "2026 BECE Integrated Science Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Social-Studies-1-2.pdf", "2026 BECE Social Studies Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Religious-and-Moral-Education-1-2.pdf", "2026 BECE RME Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-French-1-2.pdf", "2026 BECE French Paper 1 and 2"),
    ("https://colemanpublications.com/wp-content/uploads/2026/05/2026-BECE-Ghanaian-Language-Ewe-1-2.pdf", "2026 BECE Ghanaian Language Ewe Paper 1 and 2"),
]


async def main() -> int:
    db = CatalogDatabase()
    pipeline = DownloadPipeline(database=db)
    results = {"downloaded": [], "skipped": [], "rejected": []}
    for url, ctx in URLS:
        res = await pipeline.download_file(url=url, context_text=ctx)
        if res:
            results["downloaded"].append({"file": res[0].name, "subject": res[1], "sha": res[2][:12]})
        else:
            results["skipped"].append(url.rsplit("/", 1)[-1])
    db.export_catalog_json()
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
