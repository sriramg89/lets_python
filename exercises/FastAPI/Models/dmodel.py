from typing import Optional

from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.sqltypes import NullType
from fastapi import FastAPI, Depends, Request
                                              
from pydantic import BaseModel                                      
from sqlalchemy.orm import Session, session
import datetime
import sys


class UserDetails(BaseModel):                                         
    # User_ID : int
    Email : str
    Password : str
    Created_on : str

class BlogDetails(BaseModel):                                         
    # Blog_ID : int
    User_ID : int
    Title : str
    Description : str

class BlogEdit(BlogDetails):
    # Blog_ID: Optional[int]
    User_ID : Optional[int]
    Title : Optional[str]
    Description : Optional[str]
