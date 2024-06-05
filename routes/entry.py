from fastapi import APIRouter
entry_route=APIRouter()

# endpoint
@entry_route.get("/")
def api_running():
    res={
        "status":"ok",
        "message":"api is running"
    }
    return res