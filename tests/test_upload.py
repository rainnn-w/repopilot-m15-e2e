from app.upload import save_upload


def test_save_upload_roundtrip(tmp_path):
    assert save_upload(str(tmp_path / "f.bin"), b"hello")
