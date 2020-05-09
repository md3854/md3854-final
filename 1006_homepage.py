######################################
#
# Author: md3854
#
# Engi1006 final
#
######################################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def welcome():
    return render_template("1006_homepage.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

#start the server
if __name__ == "__main__":
    app.run()