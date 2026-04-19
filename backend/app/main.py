from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
import app.models  # importa todos los modelos
from app.api import auth, remittance

import time
from sqlalchemy.exc import OperationalError

app = FastAPI(title="Remesas API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    print("INICIANDO CREACIÓN DE TABLAS")

    for i in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            print("Tablas creadas correctamente")
            break
        except OperationalError:
            print("Esperando a la base de datos...")
            time.sleep(2)

# RUTAS
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(remittance.router, prefix="/remittances", tags=["Remittances"])

# ROOT
@app.get("/")
def root():
    return {"message": "API funcionando"}