from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_session
from sqlalchemy import select
from models.blogs import PostTable


router = APIRouter(
    prefix="/blogs",
    tags=["blogs"])


@router.get("/posts")
async def get_posts(session: Session = Depends(get_session)):
    posts = session.execute(select(PostTable)).scalars().all()
    return posts