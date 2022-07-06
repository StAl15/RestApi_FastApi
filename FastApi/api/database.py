from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/db"

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
