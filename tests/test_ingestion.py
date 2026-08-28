from fleetflow.ingestion import (
    load_telemetry_csv,
    validate_schema,
    validate_records,
)


SAMPLE_CSV = """vehicle_id,timestamp,speed,soc,temperature
EV01,2026-08-20 08:00:00,42,82,31
EV01,2026-08-20 08:00:01,45,81,32
EV01,2026-08-20 08:00:02,-12,81,32
EV02,2026-08-20 08:00:00,61,104,35
EV02,,62,66,36
EV03,2026-08-20 08:00:00,35,74,29
"""


def create_test_csv(tmp_path):
    file_path = tmp_path / "telemetry_sample.csv"
    file_path.write_text(SAMPLE_CSV)
    return file_path


def test_load_telemetry_csv(tmp_path):
    file_path = create_test_csv(tmp_path)

    df = load_telemetry_csv(file_path)

    assert len(df) == 6
    assert validate_schema(df) is True


def test_validate_records(tmp_path):
    file_path = create_test_csv(tmp_path)

    df = load_telemetry_csv(file_path)
    valid_df, invalid_df = validate_records(df)

    assert len(valid_df) == 3
    assert len(invalid_df) == 3

    errors = invalid_df["validation_error"].tolist()

    assert "negative_speed" in errors
    assert "invalid_soc" in errors
    assert "missing_timestamp" in errors