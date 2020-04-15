#from flask import Flask, render_template
#
#app = Flask(__name__)
#
#
#@app.route('/')
#def hello_whale():
#    return render_template("whale-hello.html")
#
#if __name__ == '__main__':
#    app.run(debug=True)
#    #app.run(debug=True, host='0.0.0.0', port=8080)
#
#
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
  html = "<h3>Hello World!</h3>"
  return html.format()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
