from flask import Flask, redirect, request, jsonify, render_template, make_response
from Tracker import amazon, flipkart
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')
@app.route('/home', methods=['POST','GET'])
def home():
    if request.method=='POST':
        url=request.form['url']
        return "recived url"
    elif request.method=='GET':
        return "Welcome to the home"
    else:
        return "Bad request method"
    

@app.route('/singletracker', methods=['POST','GET'])
def tracker():
    if request.method=='POST':
        url=request.form['url']
        pointer=request.form['tracker_name']
        print(pointer)
        if pointer=='1':
            data=amazon.main(url)
        elif pointer=='0':
            data=flipkart.main(url)
        else:
            return "Bad Url"
        return jsonify(data)
    else :
        return "Welcome to the price tracker"
@app.route('/graph',methods=['GET'])
def graph():
    data=json.load("./templates/data/data.json")
    print(data)
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return "hello"

if __name__ == '__main__':
   app.run()