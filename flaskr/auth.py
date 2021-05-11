import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

# a blueprint is a way to organize a group of related views and other code. 

# a view is a function that responds to requests at your application

# this app will have two blueprints - one for authentication
# and one for blog posts


