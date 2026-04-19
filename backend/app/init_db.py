from app.db.database import Base, engine
import app.models

print("CREANDO TABLAS...")

Base.metadata.create_all(bind=engine)

print("TABLAS CREADAS")