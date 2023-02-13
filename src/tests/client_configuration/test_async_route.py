from typing import AsyncIterator

import pytest
from httpx import AsyncClient

from src.main import app


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.anyio
async def test_main_route(client: AsyncClient) -> None:
    response = await client.get("/async/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is an asynchronous route"}
