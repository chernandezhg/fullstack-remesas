from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from app.core.security import verify_token, security

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)
    return payload