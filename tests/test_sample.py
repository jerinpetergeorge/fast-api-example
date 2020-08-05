from fastapi.testclient import TestClient

from application import demo_app

client = TestClient(demo_app)


def test_read_main():
    response = client.get("/demo/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
