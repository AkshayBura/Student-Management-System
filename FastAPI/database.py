from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = r'sqlite:///./student.db'

engine = create_engine(db_url, connect_args={"check_same_thread" : False})

localsession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()