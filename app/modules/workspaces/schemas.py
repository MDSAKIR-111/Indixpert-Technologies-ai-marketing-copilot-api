from pydantic import BaseModel


class WorkspaceCreate(BaseModel):
    workspace_name: str
    email: str
    full_name: str