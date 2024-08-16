from fastapi import FastAPI, Depends
from routers import auth
from dependencies.users.user import UserHandling
from schemas.users import UserSchema

app = FastAPI(title="Instagram API")
app.include_router(auth.router)

@app.get('/test')
async def get_test(user: UserSchema = Depends(UserHandling().developer)):
    return {
        "message": "Hello world !"
    }
