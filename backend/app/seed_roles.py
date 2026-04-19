from app.db.database import SessionLocal
from app.models.role import Role

db = SessionLocal()

roles = ["admin", "user"]

for r in roles:
    exists = db.query(Role).filter(Role.name == r).first()
    if not exists:
        db.add(Role(name=r))

db.commit()
db.close()

print("ROLES CREADOS")