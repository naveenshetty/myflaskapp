from flask import Flask
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# from my_flask_app.app import routes
from app import routes  # Import routes after initializing the app
