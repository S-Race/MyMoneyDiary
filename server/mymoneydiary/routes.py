from datetime import datetime
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from mymoneydiary import api, db
from mymoneydiary.models import User, Transaction, transaction_fields, user_fields


class Balance(Resource):
	def get(self):
		return {
			"balance": 120
		}

user_post_args = reqparse.RequestParser()
user_post_args.add_argument("username", type=str, help="username field is required", required =True )
user_post_args.add_argument("password", type=str, help="password field is required", required=True)

transaction_post_args = reqparse.RequestParser()
transaction_post_args.add_argument("date", type=str)
transaction_post_args.add_argument("transaction_type", type=bool, help="You need to specify the type of the transaction", required=True)
transaction_post_args.add_argument("amount", type=float, help="You need to specify the transaction amount", required=True)
transaction_post_args.add_argument("description", type=str)
transaction_post_args.add_argument("user_id", type=str, help="You need to specify who owns this transaction", required=True)


class TransactionRoute(Resource):
	@marshal_with(transaction_fields)
	def get(self):
		users = User.query.all()
		return users


	def post(self):
		args = transaction_post_args.parse_args()
		if not args["date"]:
			args["date"] = datetime.now()
		transaction = Transaction(date=args["date"], transaction_type=args["transaction_type"],
			amount=args["amount"],description=args["description"], user_id=args["user_id"])
		
		db.session.add(transaction)
		db.session.commit()

		return transaction, 201


	def delete(self):
		# Transaction.delete(id=)
		pass


class LoginRoute(Resource):
	def post(self):
		args = user_post_args.parse_args()
		# TODO hash the entered password before checking if the password matches
		result = User.query.get(username=args["username"], password=args["password"])
		if not result:
			return "Incorrect username or password", 400
		else:
			return "Logged in successfully", 200



class SignupRoute(Resource):
	def post(self):
		args = user_post_args.parse_args()
		# TODO hash password before saving
		user = User(username=args["username"], password=args["password"])
		db.session.add(user)
		db.session.commit()

		return "Sign up successfully", 201

api.add_resource(Balance, "/api/balance")
api.add_resource(TransactionRoute, "/api/transaction")
api.add_resource(LoginRoute, "/api/login")
api.add_resource(SignupRoute, "/api/signup")