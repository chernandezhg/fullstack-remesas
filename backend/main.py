from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user, role
from app.api import auth

app = FastAPI(title="Remesas API")

import time
from sqlalchemy.exc import OperationalError

for i in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        print("Esperando a la base de datos...")
        time.sleep(2)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "API funcionando"}