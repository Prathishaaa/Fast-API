from fastapi import FastAPI,HTTPException
from model import User,Gender,Role
from typing import List
from uuid import uuid4,UUID

app = FastAPI()
db:List[User]=[
    User(
        id=uuid4(),
        first_name="Prathi",
        last_name="Mario",
        gender=Gender.female,
        role=Role.user
    ),
    User(
        id=uuid4(),
        first_name="Prathi",
        last_name="Mario", 
        gender=Gender.female,
        role=Role.user
    )

]
"here slash means base url thst is local host 8000"
@app.get('/')
async def  message():
    return "You can do it"

# @app.get("/")
# async def my_first_web_page():
    
#     return {"my_app":"hello"}

# @app.get("/users/")
# async def fetch_users():
    
#     return db
# @app.post("/users/")
# async def register_user(user:User):
#      db.append(user)
#      return db
# @app.put("/users/")
# async def update_user(user_id:UUID,first_name:str,last_name:str):
#     for user in db:
#           if user.id==user_id:
#                user.first_name=first_name
#                user.last_name=last_name
#     return db
     
     
          
# @app.delete("/users/{user_name}")
# async def remove_user(user_name):
#     for user in db:
#           if user.first_name==user_name:
#                db.remove(user)
#                return db
#     raise HTTPException(
#          status_code=404,
#          detail=f"user with name{user_name}does not exist"
#          )



