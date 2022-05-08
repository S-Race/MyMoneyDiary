from mymoneydiary import db

class TransactionModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(100), nullable=False)
	type = db.Column(db.Boolean, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	description = db.Column(db.String(255), nullable=False)

	def __repr__(self):
		return f"Transaction(description = {self.description}, \
			amount = {self.amount}, date = {self.date}, \
				type = {'Deposit' if type else 'Withdrawal'})"