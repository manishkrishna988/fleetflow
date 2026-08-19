from fleetflow.ingestion import load_telemetry_csv, validate_schema


def test_load_telemetry_csv():
    df = load_telemetry_csv("data/raw/telemetry_sample.csv")

    assert len(df) == 6
    assert validate_schema(df) is True