from base.models import BaseModel
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey

class PostTable(BaseModel):
    __tablename__ = "blogs_post"

    user_id: Mapped[int] = mapped_column(ForeignKey(column="users_user.id"))
    description: Mapped[str]
    file: Mapped[str] = mapped_column(nullable=True)

    user: Mapped["UserTable"] = relationship(back_populates="posts")


class PostCommentTable(BaseModel):
    __tablename__ = "blogs_postcomment"

    user_id: Mapped[int] = ForeignKey(column="users_user.id")
    post_id: Mapped[int] = ForeignKey(column="blogs_post.id")
    text: Mapped[str]


class PostLikeTable(BaseModel):
    __tablename__ = "blogs_postlike"

    user_id: Mapped[int] = ForeignKey(column="users_user.id")
    post_id: Mapped[int] = ForeignKey(column="blogs_post.id")