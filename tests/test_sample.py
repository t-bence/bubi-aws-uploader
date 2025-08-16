def test_filename():
    import datetime

    from lib import compute_filename

    ts = datetime.datetime(2020, 1, 2, 10, 56, 15)
    assert compute_filename(ts) == "2020-01-02T10-56-15Z.json"
