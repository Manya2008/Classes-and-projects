#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():
    return "HIIIIII!!!!"

app.run(debug=True)

app.route("/flask")
def second_flask():
    return "I love code"

#run the application on local server
app.run(debug=True)
