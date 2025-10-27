from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_user
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User, UserRole
from app.schemas.auth import RegisterIn, LoginIn, Token, UserOut

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut, status_code=201)
def register(body: RegisterIn, db: Session = Depends(get_db)):
    # Ensure unique email
    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(400, "Email already registered")
    role = body.role if body.role in (UserRole.CLIENT, UserRole.PROVIDER, UserRole.ADMIN) else UserRole.CLIENT
    user = User(email=body.email, hashed_password=hash_password(body.password), role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserOut(
        id=user.id, email=user.email, phone=user.phone,
        role=user.role, is_verified=user.is_verified, is_active=user.is_active
    )

# Standard OAuth2 form login (username = email)
@router.post("/login", response_model=Token)
def login_form(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(sub=str(user.id))
    return Token(access_token=token)

# Optional convenience: JSON login
@router.post("/login-json", response_model=Token)
def login_json(body: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(sub=str(user.id))
    return Token(access_token=token)

@router.get("/me", response_model=UserOut)
def me(current=Depends(get_current_user)):
    return UserOut(
        id=current.id, email=current.email, phone=current.phone,
        role=current.role, is_verified=current.is_verified, is_active=current.is_active
    )
