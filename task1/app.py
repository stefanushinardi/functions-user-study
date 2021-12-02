@app.schedule(expression="* * * 1 *", param_name="timer_context") 
@app.read_cosmos_db_documents(..., param_name="users") 
def update_user_count(timer_context, users): 
    logging.info(len(users)) 
 
@app.route('/users', method=["GET"]) 
@app.read_cosmos_db_documents(..., param_name="users") 
def get_users(req, users): 
    return users 
 
@app.route('/users', method=["PUT"]) 
@app.write_cosmos_db_documents(database_name="users", container_name="container", 
                               connection_string=CONFIG_COSMOS_CONN, param_name="users") 
def add_users(req, users): 
    uuid = uuid.generate() 
    user = extract_user_and_assign_id(req, uuid) 
    users.set(user) 
    return user 
 
@static 
def extract_user_and_assign_id(req, uuid): 
    name = req.name 
    email = req.email 
    return {name :name, email: email, uuid: uuid} 
