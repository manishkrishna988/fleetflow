import pandas as pd


def load_telemetry_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def validate_schema(df):
    required_columns = {
        "vehicle_id",
        "timestamp",
        "speed",
        "soc",
        "temperature"
    }

    return required_columns.issubset(df.columns)

def validate_records(df):
    valid_records = []
    invalid_records = []

    for _, row in df.iterrows():
        errors = []

        if pd.isna(row["timestamp"]):
            errors.append("missing_timestamp")

        if row["speed"] < 0:
            errors.append("negative_speed")

        if row["soc"] < 0 or row["soc"] > 100:
            errors.append("invalid_soc")

        if errors:
            invalid_row = row.copy()
            invalid_row["validation_error"] = "; ".join(errors)
            invalid_records.append(invalid_row)
        else:
            valid_records.append(row)

    valid_df = pd.DataFrame(valid_records)
    invalid_df = pd.DataFrame(invalid_records)

    return valid_df, invalid_df