from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os
import markdown

from restful_cc.config import Config

# Create db instance
db = SQLAlchemy()

def create_app(config_class=Config):
    # Create Flask instance
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init db
    with app.test_request_context():
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
        with open(os.path.dirname(app.root_path) + '/README.md', 'r') as md:
            content = md.read()
            # Convert Markdown to HTML and return
            return markdown.markdown(content)
    
    api.add_resource(Customer, '/api/customer')
    
    return app
