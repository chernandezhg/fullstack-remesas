from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest
from app.schemas.user import UserCreate
from app.core.security import create_access_token, hash_password, verify_password
from app.api.deps import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.models.role import Role

router = APIRouter()


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_access_token({"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {"user": user}


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # 🔥 Obtener rol dinámicamente (MEJOR PRÁCTICA)
    role = db.query(Role).filter(Role.name == "user").first()

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hash_password(user.password),
        role_id=role.id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuario creado correctamente"}