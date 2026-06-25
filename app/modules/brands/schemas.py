from pydantic import BaseModel


class BrandCreate(BaseModel):
    name: str
    website: str | None = None
    industry: str | None = None


class BrandUpdate(BaseModel):
    name: str
    website: str | None = None
    industry: str | None = None


# from pydantic import BaseModel


# class BrandCreate(BaseModel):
#     name: str
#     website: str | None = None
#     industry: str | None = None


