from flask import jsonify
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser, abort
from sqlalchemy import or_

from restful_cc import db
from restful_cc.models import Customers
from restful_cc.customers.utils import issuer_check

get_args = {
    "trailing_digits": fields.Int(required=True,
                                  validate=[validate.Range(min=1000, max=9999)]),
    "leading_digits": fields.Int(required=False,
                                 validate=[validate.Range(min=1000, max=9999)]),
    "card_type": fields.Str(required=False),
    "end_date": fields.DateTime(required=False,format='%m.%Y'),
    "start_date": fields.DateTime(required=False,format='%m.%Y')
}

put_args = {
    "first_name": fields.Str(required=True),
    "email": fields.Email(required=True,
                          validate=validate.Email()),
    "trailing_digits": fields.Int(required=True,
                                  validate=[validate.Range(min=1000, max=9999)]),
    "leading_digits": fields.Int(required=False,
                                 validate=[validate.Range(min=1000, max=9999)]),
    "card_type": fields.Str(required=False),
    "end_date": fields.DateTime(required=False,format='%m.%Y'),
    "start_date": fields.DateTime(required=False,format='%m.%Y')
}
    
class Customer(Resource):

    @use_kwargs(get_args)
    def get(self,trailing_digits,
            leading_digits=None,card_type=None,end_date=None,start_date=None):

        # Check db for customers matching trailing_digits
        search = Customers.query.filter(Customers.trailing_digits == trailing_digits)
        
        # Exclude entries with mismatched data but retain null values
        if leading_digits:
            search = search.filter(or_(Customers.leading_digits == leading_digits,
                                       Customers.leading_digits == None))
            # Use leading_digits to infer card_type
            ctype = issuer_check(leading_digits//100)
            if ctype:
                search = search.filter(or_(Customers.card_type == ctype,
                                            Customers.card_type == None))
        if card_type:
            search = search.filter(or_(Customers.card_type == card_type,
                                       Customers.card_type == None))
            # Use card_type to infer leading_digits
     
            ldigs = issuer_check(str(card_type))
            if ldigs:
                search = search.filter(or_(Customers.leading_digits.in_(ldigs),
                                       Customers.leading_digits == None))       
        if end_date:
            search = search.filter(or_(Customers.end_date == end_date.strftime("%m.%Y"),
                                       Customers.end_date == None))
        if start_date:
            search = search.filter(or_(Customers.start_date == start_date.strftime("%m.%Y"),
                                       Customers.start_date == None))
        
        # If customer not found, return 404
        if not search.all():
            return {'message': 'Customer not found', 'matches': {}}, 404

        # Adding to dictionary yields unique email addresses
        matches = {}
        for c in search.all():
            matches[c.email] = c.first_name
            
        # Return possible customer matches
        return {'message': 'Possible customers found', 'matches': matches}, 200


    @use_kwargs(put_args)
    def put(self,first_name,email,trailing_digits,
            leading_digits=None,card_type=None,end_date=None,start_date=None):
        
        # Reformat dates  if provided
        if end_date:
            end_date = end_date.strftime("%m.%Y")
        if start_date:
            start_date = start_date.strftime("%m.%Y")

        # Register client in db using partial card data
        # Duplicate customers allowed as they could have registered using different card previously
        new_customer = Customers(first_name=first_name,
                                 email=email,
                                 trailing_digits=trailing_digits,
                                 leading_digits=leading_digits,
                                 card_type=card_type,
                                 end_date=end_date,
                                 start_date=start_date)
        
        db.session.add(new_customer)
        db.session.commit()

        nc = {"first_name":first_name,
              "email":email,
              "trailing_digits":trailing_digits,
              "leading_digits":leading_digits,
              "card_type":card_type,
              "end_date":end_date,
              "start_date":start_date
        }
        
        return {'message': 'Customer registered', 'data': nc}, 201

# Error handler necessary for use with Flask-RESTful as per Marshmallow documentation
@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_handlers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)
