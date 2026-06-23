import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.db.base import Base
from app.core.db.mixins import UUIDMixin


class Workspace(UUIDMixin, Base):
    __tablename__ = "workspaces"

    name: Mapped[str]

    plan: Mapped[str] = mapped_column(default="starter")

    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow
    )