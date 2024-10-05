from pydantic import EmailStr, BaseModel


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserSchema(UserBase):
    password: str


class UserSchemaSignIn(BaseModel):
    password: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr | None = None
