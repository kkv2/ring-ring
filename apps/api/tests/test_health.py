"""The health endpoint is the whole of the API at Milestone 0."""

from fastapi.testclient import TestClient

from moshi_moshi_api import __version__
from moshi_moshi_api.main import create_app


def test_health_reports_ok() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}


def test_unknown_route_is_not_found() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/nope")

    assert response.status_code == 404
