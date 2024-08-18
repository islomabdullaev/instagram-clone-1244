from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_session


router = APIRouter(
    prefix="/blogs",
    tags=["blogs"])


@router.get("/post")
async def get_posts(session: Session = Depends(get_session)):
    return []