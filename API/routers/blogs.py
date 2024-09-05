import aiofiles
from fastapi import APIRouter, Depends, status, File, UploadFile, Form
from sqlalchemy.orm import Session
from dependencies.users.user import UserHandling
from schemas.users import UserSchema
from models.users import UserTable
from schemas.blogs import PostResponseSchema
from database import get_session
from sqlalchemy import select
from models.blogs import PostTable
from directories.posts import create_dir as post_create_dir


router = APIRouter(
    prefix="/blogs",
    tags=["blogs"])


@router.get("/posts", response_model=list[PostResponseSchema])
async def get_posts(session: Session = Depends(get_session)):

    posts = session.execute(
        select(PostTable).join(UserTable)).scalars().all()
    
    return posts


@router.post("/posts")
async def create_posts(
    file: UploadFile = File(...),
    description: str = Form(...),
    user: UserSchema = Depends(UserHandling().user),
    session: Session = Depends(get_session)):
    
    post = PostTable(
        user_id=user.id,
        file=None,
        description=description,
    )
    session.add(post)
    session.flush()
    file_dir_for_django = None
    if file is not None:
        file_data = await post_create_dir(post_id=post.id, filename=file.filename)
        content = file.file.read()
        async with aiofiles.open(file_data['file_full_path'], 'wb') as out_file:
            file_dir_for_django = file_data['file_dir'] + file.filename
            await out_file.write(content)
    post.file = file_dir_for_django
    session.commit()
    session.refresh(post)

    return {
        "message": "Created !"
    }