from fastapi import FastAPI
from core.database import db_manager
import uvicorn
from api.products_router import router as products_router

app = FastAPI()


@app.on_event("startup")
def startup():
    db_manager.create_connection()
    db_manager.init_db("init.sql") # inizializzazione db
    
@app.on_event("shutdown")
def shutdown():
    db_manager.close_all()
    
app.include_router(products_router)

@app.get("/")
def get_home():
    return {"message": "home"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)