from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

SQLALCHEMY_DATABASE_URL = "postgresql://zecmmmfggksxsw:6b428ac78016a8fd7e40a750230c8b0071491b94c8b168886d889254977b97d8@ec2-54-75-184-144.eu-west-1.compute.amazonaws.com:5432/de2m99bem72evj"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

User = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String),
    Column('profile_img', LargeBinary),
    Column('email', String),
    Column('password', String)
)

Good = Table(
    "goods",
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('title', String),
    Column('description', String),
    Column('img_src', LargeBinary),
    Column('price', Float),
    Column('type', String),
    Column('color_variants', String),
    Column('parametrs', String)
)

database = Database(SQLALCHEMY_DATABASE_URL)

# ---- without async ----#
# sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
