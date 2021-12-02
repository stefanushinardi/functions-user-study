### FunctionApp
```python
class FunctionApp(app_name)
```

This class represents a Functions application. It provides the ability to register routes using the route() method and other triggers

app_name The name of the Functions app. This corresponds to the value provided when instantiating a functions object.

### Route (HTTP Trigger)

```python
route(path, **options)
```

Register a http trigger for a particular URI path. This method is to be used as a decorator. For example:

```python
from azure.functions import FunctionApp

app = FunctionApp(app_name="appname")

@app.route('/helloworld/{value}', methods=['PUT'],
            auth_level="anonymous", param_name="request")
def hello(request):
    pass
```

Parameters:

* __str path__: The path to associate with the view function. The path should only contain [a-zA-Z0-9._-] chars and curly braces for parts of the URL you would like to capture. The path should not end in a trailing slash.

* __str param_name__: The variable name used in function code that represents Function.request

* __list methods__: parameter that indicates which HTTP methods this function should accept. By default, only GET requests are supported. If you only wanted to support POST requests, you would specify methods=['POST']. If you support multiple HTTP methods in a single function (methods=['GET', 'POST'])

* __AuthLevel auth_level__: Determines what keys, if any, need to be present on the request in order to invoke the function. The authorization level can be one of the following values:

>* anonymous — No API key is required.
>* function — A function-specific API key is required. This is the default value if none is provided.
>* admin — The master key is required


### Schedule (Timer Trigger)

Create a function that’s invoked on a regular schedule.

```python
schedule(expression, param_name, **options)
```
example:

```python
@app.schedule(expression="* * * 5 *", param_name="timer_context" )
def cron_handler(timer_context):
    pass
```

Parameters: 
* __str expression__: A CRON expression that represents the time interval in which the function will be invoked

* __str param_name__: The variable name used in function code that represents Timer context.

### Azure Blob Trigger

```python
on_blob_change(path: str, connection_string: str, param_name: str)
```

Register a function to be triggered when a new or updated Azure Blob Storage is detected. This method is to be used as a decorator. For example:

```python
@app.on_blob_change(path="my_containter", connection_string="MyStorageAccount", 
                    param_name="blob_input")
def blob_handler(blob_input):
    pass
 ```
 
Parameters:

* __str path__: Path to the container to monitor in Azure Blob Storage. May be a blob name pattern.

* __str connection_string__: The name of an app setting that contains the Storage connection string to use for this binding. If the app setting name begins with "AzureWebJobs", you can specify only the remainder of the name here. For example, if you set connection to "MyStorage", the Functions runtime looks for an app setting that is named "AzureWebJobsMyStorage." If you leave connection empty, the Functions runtime uses the default Storage connection string in the app setting that is named AzureWebJobsStorage.

* __str param_name__: The name of the variable that represents the blob in function code

### Blob input binding 

```python
read_blob(path: str, connection_string: str, data_type: str, param_name: str)
```

Add a Azure Blob Storage input binding to a function.The input binding allows you to read blob storage data as input to an Azure Function.

```python
@app.read_blob(path="my_containter", connection_string="MyStorageAccount", 
                    data_type="binary", param_name="blob_input")
@app.route('/read_blob', methods=['GET'],
            auth_level="anonymous", param_name="request")
def blob_handler(request, blob_input):
    pass
```

Parameters:

* __str path__ : Path to the container to monitor in Azure Blob Storage. May be a blob name pattern.

* __str connection_string__ : The name of an app setting that contains the Storage connection string to use for this binding. If the app setting name begins with "AzureWebJobs", you can specify only the remainder of the name here. For example, if you set connection to "MyStorage", the Functions runtime looks for an app setting that is named "AzureWebJobsMyStorage." If you leave connection empty, the Functions runtime uses the default Storage connection string in the app setting that is named AzureWebJobsStorage.

* __str data_type__ : data_type specifies the underlying data type. Possible values are string, binary, or stream

* __str param_name__ : The name of the variable that represents the blob in function code

### Blob output binding

```python
def write_blob(path: str, connection_string: str, param_name: str):
```

Add a Azure Blob Storage output binding to a function. The input binding allows you to read blob storage data as input to an Azure Function.

```python
@app.read_blob(path="my_containter", connection_string="MyStorageAccount", 
                    data_type="binary", param_name="blob_input")
@app.route('/read_blob', methods=['GET'],
            auth_level="anonymous", param_name="request")
def blob_handler(request, blob_input):
    pass
```