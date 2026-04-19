from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest
from app.core.security import create_access_token

router = APIRouter()

fake_user = {
    "email": "carlos@test.com",
    "password": "123456"
}

@router.post("/login")
def login(data: LoginRequest):
    if data.email != fake_user["email"] or data.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_access_token({"sub": data.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }