from fastapi import APIRouter
from models.blog import Blog_models ,Updateblogmodels
from config.config import blogging_collection
import datetime
from bson import ObjectId
from serealizer.blog import decodeBlogs,decodeBlog

blog_route=APIRouter()
# post request
@blog_route.post("/new/blog")
def new_blog(data:Blog_models):
    doc=dict(data)
    current_date=datetime.date.today()
    doc["Date"]=str(current_date)
    res = blogging_collection.insert_one(doc)
    doc_id=str(res.inserted_id)
    return{
        "status": "good",
        "messsage":"blog posted",
        "id":doc_id
    }
    # return doc
@blog_route.get('/all/blogs')
def allBlogs():
    res=blogging_collection.find()
    decoded=decodeBlogs(res)
    return{
        "status":"ok",
        "data": decoded
    }
#665d8b49f9355c9113f56591
@blog_route.get('/blog/{_id}')
def singleBlog(_id:str):
    res = blogging_collection.find_one({"_id":ObjectId(_id)})
    decoded=decodeBlog(res)
    return{
        "status":"ok",
        "data": decoded 
    }
#update blog
@blog_route.patch('/update/{_id}')
def updateBlog(_id:str,doc:Updateblogmodels):
    req=dict(doc.model_dump(exclude_unset=True))
    
    blogging_collection.find_one_and_update(
        {"_id":ObjectId(_id)},
        {"$set":req}
        )
    return {
        "status":"ok",
        "message": "nicely updated"
    }
#delete blog
@blog_route.delete('/delete')
def deleteblog(_id:str):
    blogging_collection.find_one_and_delete(
        {"_id":ObjectId(_id)}
    )
    return{
        'status':200,
        'message':"deleted"
    }