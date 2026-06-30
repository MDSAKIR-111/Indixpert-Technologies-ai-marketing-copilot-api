from pydantic import BaseModel


class WorkspaceCreate(BaseModel):
    workspace_name: str


class WorkspaceUpdate(BaseModel):
    workspace_name: str