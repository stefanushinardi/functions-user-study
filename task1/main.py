import azure.functions as func
import datetime
from typing import List

from users import UserManager, User

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
@app.write_table_entity(table_name="UserAddLogs", connection="TABLE_STORAGE_CONNECTION_STRING", param_name="table_output", partition_key="UserAddLogs")
def add_user(req: func.HttpRequest, table_output: func.Out[str]):
    user_info = req.get_json()
    user = UserManager.add_user(user_info)

    rowKey = str(uuid.uuid4())
    data = {
        "Time": str(datetime.datetime.now())
        "PartitionKey": "UserAddLogs",
        "RowKey": rowKey
    }

    if user:
        data["Name"] = f"User added. Id {user.id}"
        table_output.set(json.dumps(data))
        return func.HttpResponse(f"User added. Id {user.id}")
    else:
        data["Name"] = f"User add failed"
        table_output.set(json.dumps(data))
        return func.HttpResponse("Could not add the new user", 400)


@app.route(path="/user/{user_id}", methods=["DELETE"])
@app.write_table_entity(table_name="UserRemoveLogs", connection="TABLE_STORAGE_CONNECTION_STRING", param_name="table_output", partition_key="UserRemoveLogs")
def remove_user(req: func.HttpRequest, user_id: str, context):
    user = UserManager.remove_user(user_id)

    rowKey = str(uuid.uuid4())
    data = {
        "Time": str(datetime.datetime.now())
        "PartitionKey": "UserAddLogs",
        "RowKey": rowKey
    }

    if user:
        data["Name"] = f"User removed. Id {user.id}"
        table_output.set(json.dumps(data))
        return func.HttpResponse(f"User removed. Id {user.id}")
    else:
        data["Name"] = f"User removal failed"
        table_output.set(json.dumps(data))
        return func.HttpResponse("Could not remove the new user", 400)
