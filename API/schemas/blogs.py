from pydantic import BaseModel

from schemas.users import UserSchema

class PostResponseSchema(BaseModel):
    id: int
    description: str
    file: str
    comments: list | None = None
    likes: list | None = None
    user: UserSchema