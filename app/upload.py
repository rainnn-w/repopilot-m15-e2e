"""Upload helper for the demo app."""

MAX_BYTES = 1_000_000


def save_upload(path: str, data: bytes) -> bool:
    """Save an upload; rejects payloads larger than MAX_BYTES."""
    if len(data) > MAX_BYTES:
        return False
    with open(path, "wb") as fh:
        fh.write(data)
    return True
