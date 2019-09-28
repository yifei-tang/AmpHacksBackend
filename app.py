import requests

import matplotlib.pyplot as plt
import os
import sys
from flask import Flask,request, url_for
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)




class HelloWorld(Resource):
    def get(self):  
        print('GET')
        my_data=request.get_json()
        print(my_data)      
        return {'Hello World':"hello"}

    def post(self):
        print('POST')
        my_data=request.get_json() #get json file here
        #process json file here 
        #return {'You sent': my_data}     
        return {'Rate': my_data['Rate'], 'Funding': my_data['Funding']}


api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)