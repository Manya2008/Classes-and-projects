from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")

def firstwebpage():
    name = "manya"
    return render_template('index.html',index_variable = name)

app.run()