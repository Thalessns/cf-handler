"""Conftest module for pytest configuration and fixtures."""
import pytest

from httpx import ASGITransport, AsyncClient

from src.app.config import app_config

app_url = f"http://{app_config.APP_HOST}:{app_config.APP_PORT}"


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "cassette_library_dir": "tests/cassettes",
        "record_mode": "once",
        "filter_headers": [("authorization", "DUMMY")],
    }


@pytest.fixture(scope="session")
async def client():
    """Fixture to provide a TestClient for FastAPI app."""
    from src.app.main import app

    async with AsyncClient(transport=ASGITransport(app=app), base_url=app_url) as client:
        yield client
