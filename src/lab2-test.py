from fastapi.testclient import TestClient
from lab2 import app

client = TestClient(app)


def test_summa():
    response = client.post("/get_summ", params={"first": 2, "second": 3})
    assert response.status_code == 200
    assert response.json() == 5


def test_sub():
    response = client.post("/get_sub", params={"first": 5, "second": 3})
    assert response.status_code == 200
    assert response.json() == 2


def test_mult():
    response = client.post("/get_mult", params={"first": 4, "second": 3})
    assert response.status_code == 200
    assert response.json() == 12


def test_div():
    response = client.post("/get_div", params={"first": 10, "second": 2})
    assert response.status_code == 200
    assert response.json() == 5.0


def test_summa_invalid_type():
    response = client.post("/get_summ", params={"first": "two", "second": 3})
    assert response.status_code == 422


def test_missing_params():
    response = client.post("/get_summ")
    assert response.status_code == 422
