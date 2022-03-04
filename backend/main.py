from typing import Any

from fastapi import FastAPI

app = FastAPI(title="Snotra | Finance tracker")


@app.get("/")
async def root() -> Any:
    return {"message": "Hello World"}
