"""Upload helper for the demo app."""

MAX_BYTES = 4_000_000  # pr-b: much larger ceiling


def save_upload(path: str, data: bytes) -> bool:
    """Save an upload; rejects payloads larger than MAX_BYTES (checked
    before reading anything into memory — fixes the large-file crash)."""
    if len(data) > MAX_BYTES:
        return False
    with open(path, "wb") as fh:
        fh.write(data)
    return True


def upload_size_ok(data: bytes) -> bool:
    """Size gate helper so callers can reject early."""
    return len(data) <= MAX_BYTES

