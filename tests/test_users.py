import pytest
from httpx import AsyncClient


def randon_email():
    from random import randint

    return f"tester{randint(1, 999999)}@example.com"


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    """
    Testa se é possivel criar um novo usuário com sucesso.
    """
    email = randon_email()
    payload = {
        "email": email,
        "password": "senha_super_secreta",
        "full_name": "Teste Automatizado",
    }

    response = await client.post("/api/v1/users/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    assert "id" in data
    assert "password" not in data


@pytest.mark.asyncio
async def test_create_user_duplicate_email(client: AsyncClient):
    """
    Testa se a API impede a criação de usuários com e-mails duplicados.
    """
    email = randon_email()
    payload = {"email": email, "password": "123", "full_name": "Duplicado"}

    await client.post("/api/v1/users/", json=payload)

    response = await client.post("/api/v1/users/", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Este e-email já está cadastrado no sistema."
