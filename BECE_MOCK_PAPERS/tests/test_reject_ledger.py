"""Tests for permanent reject ledger + download skip logic."""

from pathlib import Path

from src.classifier import FileClassifier
from src.database import CatalogDatabase


def test_rejected_content_is_permanent_and_blocks_refetch(tmp_path: Path):
    db = CatalogDatabase(db_path=tmp_path / "cat.db")
    sha = "a" * 64

    assert db.is_hash_rejected(sha) is False
    assert db.is_content_known(sha) is False

    assert db.record_rejected_content(
        sha256=sha,
        reason="not_exam_paper",
        original_url="https://example.com/lesson-notes.pdf",
        file_name="lesson-notes.pdf",
        file_type=".pdf",
        details="scheme of work",
    ) is True

    # Second insert is a no-op (same hash never duplicated)
    assert db.record_rejected_content(sha256=sha, reason="not_exam_paper") is False

    assert db.is_hash_rejected(sha) is True
    assert db.is_content_known(sha) is True

    # Even after any local file is deleted, the hash stays known
    rows = db.list_rejected_content(reason="not_exam_paper")
    assert any(r["sha256"] == sha for r in rows)


def test_kept_file_hash_is_also_known(tmp_path: Path):
    db = CatalogDatabase(db_path=tmp_path / "cat.db")
    sha = "b" * 64
    db.save_harvested_file(
        sha256=sha,
        original_url="https://example.com/bece-maths.pdf",
        file_name="bece-maths.pdf",
        file_type="pdf",
        subject="Mathematics",
        file_size=10,
        local_path="x/bece-maths.pdf",
        source_domain="example.com",
    )
    assert db.is_content_known(sha) is True
    assert db.is_hash_rejected(sha) is False


def test_reject_reason_lesson_notes_vs_exam_paper():
    notes = b"Scheme of work for term one lesson notes curriculum guide textbook"
    exam = b"BECE MOCK MATHEMATICS Paper 1 Objective questions and answers 2024"

    assert FileClassifier.reject_reason(notes, ".txt", "lesson notes scheme of work") == "not_exam_paper"
    assert FileClassifier.reject_reason(exam, ".txt", "BECE mock paper 1") is None


def test_reject_reason_blocks_non_target_subject_even_with_exam_signals():
    english_paper = b"BECE 2026 English Language Paper 1 Objective questions and answers"
    subject = FileClassifier.detect_subject_from_bytes(
        english_paper, ".txt", "2026-BECE-English-Language-1-2.pdf"
    )
    assert subject == "General_Unclassified"
    assert (
        FileClassifier.reject_reason(
            english_paper,
            ".txt",
            "2026-BECE-English-Language-1-2.pdf BECE exam paper",
            subject=subject,
        )
        == "unclassified_wrong_subject"
    )


def test_html_article_rejects_and_tombstones_non_target_subject(tmp_path: Path):
    from src.download_pipeline import DownloadPipeline

    db = CatalogDatabase(db_path=tmp_path / "cat.db")
    pipeline = DownloadPipeline(database=db)
    html = (
        "<html><body><article><h1>2026 BECE Integrated Science Paper 1 &amp; 2</h1>"
        "<p>Section A Objective Question 1: " + ("Integrated Science exam answer marks. " * 20)
        + "</p></article></body></html>"
    )
    res = pipeline.save_html_article_as_txt(
        url="https://example.com/bece-integrated-science-2026",
        title="2026 BECE Integrated Science Questions and Answers",
        html_content=html,
    )
    assert res is None
    assert db.is_url_visited("https://example.com/bece-integrated-science-2026") is True
    rejected = db.list_rejected_content(reason="unclassified_wrong_subject")
    assert len(rejected) == 1


def test_non_bece_level_wassce_shs_rejected_while_bece_allowed(tmp_path: Path):
    from src.download_pipeline import DownloadPipeline

    wassce_bytes = b"WASSCE Core Mathematics Paper 1 Objective Mock Questions and Answers"
    assert (
        FileClassifier.reject_reason(
            wassce_bytes,
            ".txt",
            "https://ghlearner.com/wassce/core-mathematics/exams/wassce-maths-mock",
            subject="Mathematics",
        )
        == "non_bece_level"
    )
    bece_bytes = b"BECE Mathematics Paper 1 Objective Mock Questions and Answers 2026"
    assert (
        FileClassifier.reject_reason(
            bece_bytes,
            ".txt",
            "https://ghlearner.com/bece/mathematics/2026/paper-1",
            subject="Mathematics",
        )
        is None
    )

    db = CatalogDatabase(db_path=tmp_path / "cat.db")
    pipeline = DownloadPipeline(database=db)
    html = (
        "<html><body><article><h1>Solve WASSCE Core Mathematics Questions &amp; Answers</h1>"
        "<p>Section A Objective Question 1: " + ("WASSCE Core Mathematics mock answer marks. " * 20)
        + "</p></article></body></html>"
    )
    res = pipeline.save_html_article_as_txt(
        url="https://ghlearner.com/wassce/core-mathematics/exams/wassce-maths-mock",
        title="Solve WASSCE Core Mathematics Questions & Answers",
        html_content=html,
    )
    assert res is None
    assert len(db.list_rejected_content(reason="non_bece_level")) == 1
