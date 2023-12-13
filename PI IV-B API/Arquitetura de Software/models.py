from sqlalchemy import Column, Integer, String
from database import Base

class Post(Base):
  __tablename__ = "posts"
  id = Column(Integer, primary_key=True)
  IBGE = Column(Integer)
  NOME = Column(String)
  LOGRADOURO = Column(String)
  BAIRRO = Column(String)
  LATITUDE = Column(String)
  LONGITUDE = Column(String)
