import json
import pytest
from src.database import CatalogDatabase


@pytest.fixture
def temp_db(tmp_path):
    db_file = tmp_path / "test_catalog.db"
    return CatalogDatabase(db_path=db_file)


def test_db_initialization(temp_db):
    assert temp_db.db_path.exists()


def test_visited_urls(temp_db):
    url = "https://ghanaeducation.org/bece-mock-2024"
    assert not temp_db.is_url_visited(url)

    temp_db.record_url_visited(url, 200)
    assert temp_db.is_url_visited(url)


def test_save_harvested_file_and_deduplication(temp_db, tmp_path):
    fake_file = tmp_path / "math_mock.pdf"
    fake_file.write_bytes(b"dummy pdf content")

    sha256 = "11223344556677889900aabbccddeeff11223344556677889900aabbccddeeff"
    saved = temp_db.save_harvested_file(
        sha256=sha256,
        original_url="https://passco.com.gh/math.pdf",
        file_name="Mathematics_2024_Mock.pdf",
        file_type=".pdf",
        subject="Mathematics",
        file_size=fake_file.stat().st_size,
        local_path=str(fake_file),
        source_domain="passco.com.gh"
    )
    assert saved is True
    assert temp_db.is_hash_seen(sha256) is True

    # Duplicate save should be rejected (returns False)
    duplicate_saved = temp_db.save_harvested_file(
        sha256=sha256,
        original_url="https://passco.com.gh/math_copy.pdf",
        file_name="Mathematics_2024_Mock_copy.pdf",
        file_type=".pdf",
        subject="Mathematics",
        file_size=fake_file.stat().st_size,
        local_path=str(fake_file),
        source_domain="passco.com.gh"
    )
    assert duplicate_saved is False


def test_export_catalog_json(temp_db, tmp_path):
    json_path = tmp_path / "catalog.json"
    temp_db.save_harvested_file(
        sha256="aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899",
        original_url="https://becezone.com/ict.docx",
        file_name="Computing_Mock.docx",
        file_type=".docx",
        subject="Computing_ICT",
        file_size=1024,
        local_path="/tmp/ict.docx",
        source_domain="becezone.com"
    )
    records = temp_db.export_catalog_json(export_path=json_path)
    assert len(records) == 1
    assert records[0]["subject"] == "Computing_ICT"
    assert records[0]["file_type"] == "docx"
    assert records[0]["is_marking_scheme"] == 0
    assert json_path.exists()


def test_file_type_normalization_on_insert_and_startup_migration(tmp_path):
    import sqlite3

    db_file = tmp_path / "legacy_ft.db"
    db = CatalogDatabase(db_path=db_file)

    db.save_harvested_file(
        sha256="1" * 64,
        original_url="https://example.com/a.pdf",
        file_name="CAD_Mock.pdf",
        file_type=" ..PDF ",
        subject="CAD",
        file_size=512,
        local_path="/tmp/CAD_Mock.pdf",
        source_domain="example.com",
    )
    db.record_rejected_content(
        sha256="2" * 64,
        reason="not_exam_paper",
        original_url="https://example.com/notes.txt",
        file_name="notes.txt",
        file_type=".TXT",
    )
    assert db.get_stats()["file_types"] == {"pdf": 1}
    assert db.list_rejected_content()[0]["file_type"] == "txt"

    # Simulate an ad-hoc raw SQL insert with a leading dot, then re-open CatalogDatabase
    with sqlite3.connect(str(db_file)) as conn:
        conn.execute(
            "INSERT INTO harvested_files "
            "(sha256, original_url, file_name, file_type, subject, file_size, local_path, source_domain) "
            "VALUES (?, 'local://cad', 'raw.pdf', '.pdf', 'CAD', 100, '/tmp/raw.pdf', 'local');"
            ,
            ("3" * 64,),
        )
        conn.execute(
            "UPDATE rejected_content SET file_type = '.txt' WHERE sha256 = ?;",
            ("2" * 64,),
        )

    reopened = CatalogDatabase(db_path=db_file)
    assert reopened.get_stats()["file_types"] == {"pdf": 2}
    assert reopened.list_rejected_content()[0]["file_type"] == "txt"
