import azure.functions as func
from users import UserManager, User
from typing import List

app = func.FunctionsApp("dummy-function-app", AuthLevel="FunctionAppLevelAuth")


@app.route(path="/user", methods=["GET"])
def get_users(req: func.HttpRequest, user_id: str, context):
    users: List[User] = UserManager.get_users()
    return func.HttpResponse(users)


@app.route(path="/user/{user_id}", methods=["GET"])
def get_user(req: func.HttpRequest, user_id: str, context):
    user: User = UserManager.get_user(user_id)
    return func.HttpResponse(user)


@app.route(path="/user", methods=["POST"])
def add_user(req: func.HttpRequest):
    user_info = req.get_json()
    user = UserManager.add_user(user_info)
    if user:
        return func.HttpResponse(f"User added. Id {user.id}")
    else:
        return func.HttpResponse("Could not add the new user", 400)


@app.route(path="/user/{user_id}", methods=["DELETE"])
def remove_user(req: func.HttpRequest, user_id: str, context):
    user = UserManager.remove_user(user_id)
    if user:
        return func.HttpResponse(f"User removed. Id {user.id}")
    else:
        return func.HttpResponse("Could not remove the new user", 400)

