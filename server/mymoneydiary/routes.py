from flask_restful import Resource, reqparse, abort, fields, marshal_with
from mymoneydiary import api

class HelloWorld(Resource):
	def get(self):
		return {"data": "Hello World"}

class Balance(Resource):
	def get(self):
		return {
			"balance": 120
		}

api.add_resource(HelloWorld,"/api/helloworld")
api.add_resource(Balance,"/api/balance")