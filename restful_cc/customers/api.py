from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, parser, abort

from restful_cc import db

class Customer(Resource):

    get_args = {
        "trailing_digits": fields.Int(required=True,
                                      validate=[validate.Range(min=1000, max=9999)]),
        "leading_digits": fields.Int(required=False,
                                     validate=[validate.Range(min=1000, max=9999)]),
        "card_type": fields.Str(required=False),
        "end_date": fields.Date(required=False),
        "start_date": fields.Date(required=False)
    }

    @use_args(get_args)
    def get(self,args):
        # Check db for matching customers
        
        # If customer not found, return 404.
        #if not (customer in db):
        #return {'message': 'Customer not found', 'data': {}}, 404

        # Return possible customer matches
        matches = {}
        return {'message': 'Possible customers found', 'matches': matches}, 200

    put_args = {
        "first_name": fields.Str(required=True),
        "email": fields.Email(required=True,
                              validate=validate.Email()),
        "trailing_digits": fields.Int(required=True,
                                      validate=[validate.Range(min=1000, max=9999)]),
        "leading_digits": fields.Int(required=False,
                                     validate=[validate.Range(min=1000, max=9999)]),
        "card_type": fields.Str(required=False),
        "end_date": fields.Date(required=False),
        "start_date": fields.Date(required=False)
    }

    @use_args(put_args)
    def put(self,args):
        # Register client in db using partial card data
        return {'message': 'Customer registered', 'data': args}, 201

# Error handler necessary for use with Flask-RESTful as per Marshmallow documentation
@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_handlers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)
