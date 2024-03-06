from flask import Flask #from the flask module import the flask class
#oop = object oriented paradigm
app = Flask(__name__) # Create an instance of Flask into app (now an objaect) "dunder method"

@app.get("/") #Flask deceorator that maps routes to view functions
def index():  #In flask, "wrapped" functions are referred to as "view functions"
    me = {    #python dictionary (key-value pairs)
        "first_name": "Corey",
        "last_name": "Johnson",
        "hobbies": "Motorcycles",
        "online": True
    }
    return me # In flask, whenm you return a directory it is automatically converted to JSON
