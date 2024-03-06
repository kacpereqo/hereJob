import uvicorn
from src.utils import create_app

app = create_app()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
