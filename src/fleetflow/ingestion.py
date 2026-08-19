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