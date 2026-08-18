from pydantic import BaseModel, Field, ConfigDict, EmailStr

from datetime import datetime



class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr =Field(min_length=1, max_length=120)
    
    
class UserCreate(UserBase):
    password: str = Field(min_length=6)

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    image_path: str | None
    image_file: str | None


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    user_id: int

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    date_posted: datetime
    author: UserResponse