from fastapi import FastAPI
from routers import auth

app = FastAPI(title="Instagram API")
app.include_router(auth.router)

@app.get('/test')
async def get_test():
    return {
        "message": "Hello world !"
    }
