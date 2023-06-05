from pydantic import BaseModel, EmailStr
from beanie import Document, Link
from typing import Optional, List
from models.events import Event


class User(Document):
    email: EmailStr
    password: str

    class Collection:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# 사용자 로그인 모델(UserSignIn -> TokenResponse)
class TokenResponse(BaseModel):
    access_token: str
    token_type: str