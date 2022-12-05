# using flask_restful
from flask import Flask, jsonify, request,  make_response
import json 
from flask_restful import Resource, Api
from numpy import random
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return make_response(jsonify({"Instructions":"To get the energy consumption a 'client_id' is required"}), 200)
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json(force=True)     # status code
        if "client_id" in data: 
            result = 3000
            return make_response(jsonify({"energy consumption":random.randint(1,201)}), 200)
        
        return make_response(jsonify({"error":" 'client_id' required"}), 400)
       
  
# another resource to calculate the square of a number
class Square(Resource):
  
    def get(self, num):
  
        return jsonify({'square': num**2})
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/consumption')
api.add_resource(Square, '/square/<int:num>')


  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)