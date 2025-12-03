import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_access_token(client: AsyncClient):
    """
    Testa o fluxo completo: Cria usuário -> Faz Login -> Recebe Token.
    """

    email = "login_test@example.com"
    password = "password123"

    from random import randint

    email = f"login_{randint(1, 100000)}@example.com"

    await client.post("/api/v1/users/", json={"email": email, "password": password})

    login_data = {"username": email, "password": password}

    response = await client.post("/api/v1/access-token", data=login_data)

    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"
