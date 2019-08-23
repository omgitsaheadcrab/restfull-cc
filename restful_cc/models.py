from restful_cc import db

class Customer(db.Model):

    __tablename__ = "customer"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20, nullable=False))
    email = db.Column(db.String(120, nullable=False))
    trailing_digits = db.Column(db.Integer(4, nullable=False))
    leading_digits = db.Column(db.Integer(4, nullable=True))
    card_type = db.Column(db.String(20, nullable=True))
    start_date = db.Column(db.String(7, nullable=True))
    end_date = db.Column(db.String(7, nullable=True))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
