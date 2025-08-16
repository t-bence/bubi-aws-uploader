from datetime import datetime


def compute_filename(ts: datetime) -> str:
    # Format: 2020-01-02T10-56-15Z.json
    return ts.strftime("%Y-%m-%dT%H-%M-%SZ.json")
