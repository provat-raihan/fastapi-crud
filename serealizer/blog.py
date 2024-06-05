# for one  
def decodeBlog(doc) ->dict :
    return{
        "_id":str(doc["_id"]),
        "title":doc["title"],
        "subTitle" : doc["subTitle"],
        "content": doc["content"],
        "author": doc["author"],
        "tags": doc["tags"],
        "Date": doc["Date"]
    }
# eta shob blogs ke niye then looping koira ekta ekta kore alada kore
def decodeBlogs(docs) ->list:
    return [decodeBlog(doc) for doc in docs]