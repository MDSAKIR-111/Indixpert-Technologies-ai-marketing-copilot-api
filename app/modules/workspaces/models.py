import datetime
import uuid

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.core.db.base import Base


class Workspace(Base):
    __tablename__ = "workspaces"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str]

    plan: Mapped[str] = mapped_column(
        default="starter"
    )

    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )