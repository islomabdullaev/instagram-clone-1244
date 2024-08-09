from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


class UserTable(Base):
    __tablename__ = 'users_user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    first_name: Mapped[str]
    last_name: Mapped[str]
    phone: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str]
    gender: Mapped[str]
    date_of_birth: Mapped[date]