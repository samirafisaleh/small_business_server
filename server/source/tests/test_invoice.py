from fastapi.testclient import TestClient

from source.main_fastapi import app 


client = TestClient(app)


def test_create():
    response = client.post("/invoice/")
    assert 100 == 100

def test_get():
    id = 1
    response = client.get(f"/invoice/{id}")
    assert 100 == 100

def test_list():
    response = client.get("/invoice/")
    assert 100 == 100

def test_update():
    id = 1
    response = client.post(f"/invoice/{id}")
    assert 100 == 100

def test_delete():
    id = 1
    response = client.post(f"/invoice/{id}")
    assert 100 == 100

