import pytest
from httpx import AsyncClient
from app.main import app, fibonacci

@pytest.mark.parametrize("n,expected", [(1,1), (2,1), (10,55), (99,218922995834555169026)])
def test_fibonacci_logic(n, expected):
    assert fibonacci(n) == expected

@pytest.mark.asyncio
async def test_api_ok():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/fib", params={"n":10})
    assert res.status_code == 200 and res.json()["result"] == 55

@pytest.mark.asyncio
async def test_api_bad():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/fib", params={"n":-1})
    assert res.status_code == 400
    assert res.json() == {"status":400,"message":"n must be a positive integer"}
