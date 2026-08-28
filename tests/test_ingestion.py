from fleetflow.ingestion import (
    load_telemetry_csv,
    validate_schema,
    validate_records,
)


def test_load_telemetry_csv():
    df = load_telemetry_csv("data/raw/telemetry_sample.csv")

    assert len(df) == 6
    assert validate_schema(df) is True


def test_validate_records():
    df = load_telemetry_csv("data/raw/telemetry_sample.csv")

    valid_df, invalid_df = validate_records(df)

    assert len(valid_df) == 3
    assert len(invalid_df) == 3

    errors = invalid_df["validation_error"].tolist()

    assert "negative_speed" in errors
    assert "invalid_soc" in errors
    assert "missing_timestamp" in errors