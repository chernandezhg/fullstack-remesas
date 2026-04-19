from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user, role

app = FastAPI(title="Remesas API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API funcionando"}