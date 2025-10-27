from pydantic import BaseModel, EmailStr

class RegisterIn(BaseModel):
    email: EmailStr
    password: str
    role: str = "CLIENT"  # optional; defaults to CLIENT

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    id: int
    email: EmailStr | None = None
    phone: str | None = None
    role: str
    is_verified: bool
    is_active: bool
