from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer

from dependencies.JWT.handlers import JWTHandler

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/signin")

w