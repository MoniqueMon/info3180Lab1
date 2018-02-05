import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return 'My home page'
@app.route("/<myname>")
def hello(myname='person'):
    return "Hello {0}".format(myname)
    # return render_template('hello.html', name=myname)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080) 
