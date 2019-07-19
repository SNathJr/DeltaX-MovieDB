# non-flask python imports
import os
import datetime

# flask based and other python script imports
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_session import Session
from flask_bcrypt import generate_password_hash, check_password_hash
from models import *

# cloudinary imports for image CDN
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Check for environment variable DATABASE_URL
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # db as defined in models.py


# Index page route
@app.route('/')
def index():
    return "Hello DeltaX"