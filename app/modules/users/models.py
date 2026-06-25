import datetime
import uuid

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.core.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False,
    )

    full_name: Mapped[str | None]

    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )