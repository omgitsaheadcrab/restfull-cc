from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os
import markdown

from restful_cc.config import gen_connection_string

# Create db 
db = SQLAlchemy()

# Create Flask instance
app = Flask(__name__)

# Init db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = gen_connection_string()
app.app_context().push()

db.init_app(app)
db.create_all()
    
# Create API
api = Api(app)

from restful_cc.customers.api import Customer

@app.route("/",methods=['GET'])
@app.route("/api",methods=['GET'])
def index():
    """Display API documentation"""
    # Open Markdown README and read()
    with open(os.path.dirname(app.instance_path) + '/README.md', 'r') as md:
        content = md.read()
        # Convert Markdown to HTML and return
        return markdown.markdown(content)
        
api.add_resource(Customer, '/api/customer')
