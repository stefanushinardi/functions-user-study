import azure.functions as func


app = func.FunctionsApp("dummy-function-app", AuthLevel="FunctionAppLevelAuth")

"""  
* HTTP Trigger that returns hello world 
* Timer trigger that uses Blob input Binding for to read some file in the blob 
"""