
from fastapi import FastAPI, Depends, Request
from sqlalchemy.sql.expression import null, select,join,outerjoin, true  
import dtables                                                  
from dbase import SessionLocal, engine
from pydantic import BaseModel                                      
from dtables import User, Blog
from sqlalchemy.orm import Session
import datetime
from fastapi.encoders import jsonable_encoder
import sys
# from fastapi.templating import Jinja2Templates


user = FastAPI()                                                           
blog = FastAPI()
# templates=Jinja2Templates(directory="templates")   

def get_db():                                                           
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()        

dtables.Base.metadata.create_all(bind=engine)


class UserDetails(BaseModel):                                         
    User_ID : int
    Email : str
    Password : str
    Created_on : str

class BlogDetails(BaseModel):                                         
    Blog_ID : int
    User_ID : int
    Title : str
    Description : str
  

@user.get("/all")                                                              
def User_Details(db: Session = Depends(get_db)):
        data=db.query(User).all()
        return {"data":data}

@user.get("/{entry}")                                                
async def User_by_entry(entry: str, db: Session = Depends(get_db)):
    
    if(entry.isnumeric()==1):
       
        data = db.query(User).filter(User.User_ID == int(entry)).all()
        return {"data":data}

    else:

        data = db.query(User).filter(User.Email == entry).all()
        return {"data":data}     

@user.post("/")                                                    
async def create_user(detail_request: UserDetails, db: Session = Depends(get_db)):

    post = User()                                                               
    post.User_ID = detail_request.User_ID                                         
    post.Email=detail_request.Email
    post.Password=detail_request.Password
    post.Created_on=detail_request.Created_on
        
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "User details added to the database"
    }    

@blog.post("/")                                                    
async def create_blog(detail_request: BlogDetails, db: Session = Depends(get_db)):

    post = Blog()                                                               
    post.Blog_ID = detail_request.Blog_ID
    post.User_ID = detail_request.User_ID                                         
    post.Title=detail_request.Title
    post.Description=detail_request.Description
    
        
    db.add(post)
    db.commit()
    return {
        "code": "success",
        "message": "Blog details added to the database"
    }    

@blog.put("/{item_id}", response_model=BlogDetails)
async def update_blog(item_id: str, item: BlogDetails,db: Session = Depends(get_db)):
    items=Blog()
    data=db.query(Blog).all()
    update_item_encoded = jsonable_encoder(item)
    return update_item_encoded
    # data[item_id] = update_item_encoded
    # return data

@blog.get("/{UID}")                                                
async def job_dataid(UID: int, db: Session = Depends(get_db)):

        data = db.query(Blog).filter(Blog.Blog_ID == int(UID)).all()
        return {"data":data}

@blog.delete("/{UID}")                                             
async def job_databyID(UID:int, db: Session = Depends(get_db)):
   
    db.query(Blog).filter(Blog.User_ID == UID).delete()
    db.commit()
    data=db.query(Blog).all()
    return {
        "code": "success",
        "message": "Blog was deleted from the database"} 

