from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# import models
from app.modules.users.models import User
from app.modules.workspaces.models import Workspace
from app.modules.workspaces.membership import WorkspaceMember