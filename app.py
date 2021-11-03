from flask import Flask, render_template, url_for, request, redirect
from flask_restful import Api, Resource, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

#Creating a new flask app
app = Flask(__name__)
api = Api(app)

# Database configuration and model for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)

# db.create_all() # Should be removed after creating the database, not commented. I wanted to leave this line to show that it was used.
from backend.routes import *

if __name__ == "__main__":
    app.run(debug=True)  # TODO: To remove debug when done
