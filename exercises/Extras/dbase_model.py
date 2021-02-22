import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy import Boolean, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import DateTime

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"                              
                                                                                
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()     


class User(Base):                                                                       
    __tablename__ = "User"                                                              
                                                                                        
    User_ID = Column(Integer, primary_key=True)
    Email = Column(String)
    Password = Column(String)
    Created_on = Column(String)

class Blog(Base):
    __tablename__="Blog"    
    Blog_ID = Column(String, primary_key=True)
    User_ID = Column(Integer,ForeignKey("User.User_ID"))
    Title = Column(String)
    Description = Column(String)
