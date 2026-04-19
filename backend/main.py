from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user, role
from app.api import auth

app = FastAPI(title="Remesas API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "API funcionando"}