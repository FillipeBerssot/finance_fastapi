from typing import Any

from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    """
    Classe base declarativa, de onde todos os modelos herdarão."
    """

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Any
