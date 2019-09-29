import requests

import matplotlib.pyplot as plt
import os
import sys
from flask import Flask,jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS']='Content-Type'

@app.route('/',methods=['GET','POST'])
@cross_origin()

def index():
    if(request.method=="POST"):
        print("Post")
        my_data=request.get_json()
        return jsonify({'You sent':my_data}),201
    else:
        return jsonify({"Test":"Hello World"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)

# class HelloWorld(Resource):
#     def get(self):  
#         print('GET')
#         my_data=request.get_json()
#         print(my_data)      
#         return {'Hello World':"hello"}

#     def post(self):
#         print('POST')
#         my_data=request.get_json() #get json file here
#         #process json file here 
#         #return {'You sent': my_data}     
#         return {'Rate': my_data['Rate'], 'Funding': my_data['Funding']}


# api.add_resource(HelloWorld,'/')

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", debug=False)