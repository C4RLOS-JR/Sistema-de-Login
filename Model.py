from unittest.mock import Base
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


USUARIO = 'root'
SENHA = ''
HOST = 'localhost'
PORT = '3306'
DB = 'sistema_de_login'
CONNECT = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONNECT, echo=True)
Session = sessionmaker(bind=engine)
session = Session
Base = declarative_base()


class Cadastro(Base):
  __tablename__='Cadastro'
  id = Column(Integer, primary_key=True)
  nome = Column(String(50))
  email = Column(String(20))
  senha = Column(String(8))


class Login:
  pass

Base.metadata.create_all(engine)