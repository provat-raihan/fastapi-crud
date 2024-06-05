from pydantic import BaseModel
from typing import Optional
class Blog_models(BaseModel):
    title: str
    subTitle : str
    content: str
    author: str
    tags: list

class Updateblogmodels(BaseModel):
    title:Optional [str] = None
    subTitle :Optional [str] = None
    content: Optional [str] = None
    author: Optional [str]  = None
    tags:Optional [list] = None