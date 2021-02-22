

from Models import dmodel 
import DB_Models.dbase_model
from fastapi import FastAPI, Depends, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, session
# from Models.dmodel import get_db
from DB_Models.dbase_model import User,Blog
from Models.dmodel import UserDetails, BlogDetails, BlogEdit
from DB_Models.dbase_model import SessionLocal, engine


user = FastAPI()                                                           
blog = FastAPI()
 

def get_db():                                                           
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()        

DB_Models.dbase_model.Base.metadata.create_all(bind=engine)

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
       
@blog.get("/")
def abc(db: Session = Depends(get_db)):
    data=db.query(Blog).all()
    return data    

@blog.post("/{item_id}")
async def update_blog(item_id: int, item: BlogEdit, db: Session = Depends(get_db)):
    
    update_item_encoded = {i: jsonable_encoder(item)[i] for i in jsonable_encoder(item) if jsonable_encoder(item)[i]!=None}
    db.query(Blog).filter(Blog.User_ID==int(item_id)).update(update_item_encoded)
    
    db.commit()
    data= db.query(Blog).filter(Blog.User_ID==int(item_id)).first()
    return data

@blog.get("/{UID}")                                                
async def job_dataid(UID: int, db: Session = Depends(get_db)):

        data = db.query(Blog).filter(Blog.User_ID == int(UID)).all()
        return {"data":data}

@blog.delete("/{UID}")                                             
async def job_databyID(UID:int, db: Session = Depends(get_db)):
   
    db.query(Blog).filter(Blog.User_ID == UID).delete()
    db.commit()
    data=db.query(Blog).all()
    return {
        "code": "success",
        "message": "Blog was deleted from the database"} 

