from typing import Optional, List
from pydantic import BaseModel

class PostBaseSchema(BaseModel):
  IBGE: int
  NOME: str
  LOGRADOURO: str
  BAIRRO: str
  LATITUDE: str
  LONGITUDE: str

class PostCreateSchema(PostBaseSchema):
  pass

class PostSchema(PostBaseSchema):
  id: Optional[int] = None

  class Config:
    from_attributes = True

class PostListCreateSchema(BaseModel):
  posts: List[PostCreateSchema]
