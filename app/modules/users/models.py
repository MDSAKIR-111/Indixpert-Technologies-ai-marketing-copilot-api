import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.db.base import Base
from app.core.db.mixins import UUIDMixin


class User(UUIDMixin, Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)

    full_name: Mapped[str | None]

    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )