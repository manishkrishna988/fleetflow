# FleetFlow

FleetFlow is a production-style data engineering project focused on building an end-to-end telemetry data platform for connected electric vehicles.

The project will ingest raw vehicle telemetry, validate and transform noisy sensor data, organize data using a Medallion-style architecture, and expose analytics-ready datasets for fleet monitoring and future predictive-health applications.

## Project Goals

- Build reliable batch and streaming data pipelines.
- Practice SQL and relational data modelling.
- Implement Bronze, Silver, and Gold data layers.
- Learn Docker, dbt, Apache Airflow, PySpark, Kafka, and Databricks concepts.
- Add automated testing and CI/CD.
- Build a portfolio project that reflects real-world data engineering practices.

## Current Status

FleetFlow currently includes:

* A structured Python project using a `src/` layout.
* Local development with Python 3.13 and an isolated virtual environment.
* CSV-based telemetry ingestion using pandas.
* Basic schema validation for required telemetry fields.
* Record-level data quality checks for missing timestamps, negative speeds, and invalid battery state-of-charge values.
* Separation of valid and invalid telemetry records.
* Automated tests with pytest.
* Self-contained test data for reproducible local and CI execution.
* GitHub Actions CI that automatically runs tests on pushes and pull requests to `main`.

The next development milestone is to persist validated telemetry into PostgreSQL and introduce relational data modelling for fleet and telemetry entities.
