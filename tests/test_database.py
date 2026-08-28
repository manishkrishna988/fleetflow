import pytest

from fleetflow.database import get_connection


@pytest.mark.integration
def test_database_connection():
    connection = get_connection()

    assert connection is not None

    connection.close()