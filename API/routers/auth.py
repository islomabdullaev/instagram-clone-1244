from fastapi import APIRouter, Depends
from database import get_session
from sqlalchemy.orm import Session
from models.users import UserTable
from sqlalchemy import select

router = APIRouter(
    prefix="/auth",
    tags=['auth'])

@router.get('/users')
async def get_users(session: Session =  Depends(get_session)):
    users = session.execute(select(UserTable)).scalars().all()
    return users
