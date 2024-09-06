import aiofiles
from fastapi import APIRouter, Depends, status, File, UploadFile, Form, HTTPException, Response
from sqlalchemy.orm import Session, selectinload
from dependencies.users.user import UserHandling
from schemas.users import UserSchema
from models.users import UserTable
from schemas.blogs import PostResponseSchema, PostCommentCreateSchema
from database import get_session
from sqlalchemy import select
from models.blogs import PostTable, PostCommentTable
from directories.posts import create_dir as post_create_dir
from fastapi.responses import JSONResponse



router = APIRouter(
    prefix="/blogs",
    tags=["blogs"])


@router.get("/posts")
async def get_posts(session: Session = Depends(get_session)):

    posts = session.execute(
        select(PostTable).options(
            selectinload(PostTable.comments)
        ).join(UserTable)).scalars().all()
    print(posts)
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


@router.post("/posts/comments")
async def create_posts(
    data: PostCommentCreateSchema,
    user: UserSchema = Depends(UserHandling().user),
    session: Session = Depends(get_session)):

    post = session.execute(
        select(PostTable).where(PostTable.id == data.post_id)
        ).scalar()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Post does not exist !")

    comment = PostCommentTable(
        post_id=post.id,
        user_id=user.id,
        text=data.text
    )
    
    session.add(comment)
    session.commit()
    session.refresh(comment)

    return JSONResponse(content={
        "message": "Created Successfully !"
    }, status_code=status.HTTP_201_CREATED)
