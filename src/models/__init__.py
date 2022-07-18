import os
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


engine = create_engine(os.environ.get("DATABASE_URL",'postgresql://postgres:postgres@localhost:5433/code_graper'))
Base = declarative_base()

