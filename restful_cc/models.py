from restful_cc import db
from fstrings import f

class Customers(db.Model):

    __tablename__ = "customers"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    trailing_digits = db.Column(db.Integer, nullable=False)
    leading_digits = db.Column(db.Integer, nullable=True)
    card_type = db.Column(db.String(20), nullable=True)
    start_date = db.Column(db.String(7), nullable=True)
    end_date = db.Column(db.String(7), nullable=True)

    def __repr__(self):
        return f("Customers('{self.first_name}', '{self.email}', '{self.trailing_digits}', '{self.leading_digits}', '{self.card_type}', '{self.start_date}', '{self.end_date}')")
