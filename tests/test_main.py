import httpx2
import pytest

from app.main import app


def make_client() -> httpx2.AsyncClient:
    transport = httpx2.ASGITransport(app=app)
    return httpx2.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.anyio
async def test_root_returns_message():
    async with make_client() as client:
        response = await client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is running"}
    assert "X-Process-Time" in response.headers


@pytest.mark.anyio
async def test_list_items():
    async with make_client() as client:
        response = await client.get("/items", headers={"X-Api-Version": "v1"})

    assert response.status_code == 200
    assert response.json()[0]["name"] == "Notebook"


@pytest.mark.anyio
async def test_get_missing_item():
    async with make_client() as client:
        response = await client.get("/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item 999 was not found"


@pytest.mark.anyio
async def test_create_item():
    async with make_client() as client:
        response = await client.post(
            "/items",
            json={"name": "Tea", "price": 3.25, "in_stock": True},
        )

    assert response.status_code == 201
    assert response.json()["name"] == "Tea"


@pytest.mark.anyio
async def test_create_item_with_trailing_slash():
    async with make_client() as client:
        response = await client.post(
            "/items/",
            json={"name": "Milk", "price": 2.75, "in_stock": True},
        )

    assert response.status_code == 201
    assert response.json()["name"] == "Milk"


@pytest.mark.anyio
async def test_validation_error_has_custom_shape():
    async with make_client() as client:
        response = await client.post("/items", json={"name": "A", "price": -1})

    assert response.status_code == 422
    assert response.json()["message"] == "The request data is not valid."
