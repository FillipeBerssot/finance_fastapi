from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import user as crud_user
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Endpoint para criar um novo usuário.
    """
    user_exists = await crud_user.get_user_by_email(db, email=user_in.email)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este e-email já está cadastrado no sistema.",
        )

    new_user = await crud_user.create_user(db, user_in)

    return new_user
