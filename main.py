from fastapi import FastAPI
from routes.entry import entry_route
from routes.blog import blog_route
app=FastAPI()
app.include_router(entry_route)
app.include_router(blog_route)