from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import security
from app.crud import user as crud_user
from app.db.session import get_db
from app.schemas.token import Token

router = APIRouter()


@router.post("/access-token", response_model=Token)
async def login_access_token(
    db: Annotated[AsyncSession, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    """
    Login com token compatível com OAuth2.
    """
    user = await crud_user.authenticate(
        db, email=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail ou senha incorretos.",
        )

    acces_token_expires = timedelta(minutes=30)
    acces_token = security.create_access_token(
        subject=user.id, expires_delta=acces_token_expires
    )

    return {
        "access_token": acces_token,
        "token_type": "bearer",
    }
