from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate


async def get_user_by_email(db: AsyncSession, email: str):
    """
    Busca um usuário pleo email.
    """
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: UserCreate):
    """
    Cria um novo usuário no banco de dados.
    """
    hashed_password = get_password_hash(user.password)

    db_user = User(
        email=user.email,
        password_hash=hashed_password,
        full_name=user.full_name,
    )

    db.add(db_user)
    await db.commit()

    await db.refresh(db_user)
    return db_user
