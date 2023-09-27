from flask import Blueprint,Flask,render_template, request 
from .sample import person

register = Blueprint('signup', __name__)
@register.route('/signup')

def home():
    return render_template('signup.html')
