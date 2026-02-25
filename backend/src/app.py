from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import db_manager
import uvicorn
from api.products_router import router as products_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    db_manager.create_connection()
    db_manager.init_db("init.sql")
    yield
    # shutdown
    db_manager.close_all()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_router)

@app.get("/")
def get_home():
    return {"message": "home"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)