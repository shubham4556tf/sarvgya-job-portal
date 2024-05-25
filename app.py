from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>this is the test funtion</p>"
if __name__=="__main__":
    
     app.run(host='0.0.0.0',port=50100,debug=True)