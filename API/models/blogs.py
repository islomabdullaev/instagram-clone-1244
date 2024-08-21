from base.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class PostTable(BaseModel):
    __tablename__ = "blogs_post"

    user_id: Mapped[int] = ForeignKey(column="users_user.id")
    description: Mapped[str]
    file: Mapped[str]

    user: Mapped["UserTable"] = relationship(back_populates="user")


class PostCommentTable(BaseModel):
    __tablename__ = "blogs_postcomment"

    user_id: Mapped[int] = ForeignKey(column="users_user.id")
    post_id: Mapped[int] = ForeignKey(column="blogs_post.id")
    text: Mapped[str]


class PostLikeTable(BaseModel):
    __tablename__ = "blogs_postlike"

    user_id: Mapped[int] = ForeignKey(column="users_user.id")
    post_id: Mapped[int] = ForeignKey(column="blogs_post.id")