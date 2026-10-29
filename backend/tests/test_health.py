from backend.app.main import app
from fastapi.testclient import TestClient


def test_system_health_endpoint_returns_platform_status() -> None:
    with TestClient(app) as client:
        response = client.get("/system/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "platform": "ALPIP"}
