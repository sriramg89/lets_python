import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import DateTime

from dbase import Base


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



