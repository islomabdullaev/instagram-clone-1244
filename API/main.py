from fastapi import FastAPI

app = FastAPI(title="Instagram API")


@app.get('/test')
async def get_test():
    return {
        "message": "Hello world !"
    }
