
from flask import Blueprint, render_template, request
from .models import get_food_data

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    # Extract data from request and process
    fdc_id = request.form.get('fdcId')
    food_data = get_food_data(fdc_id)
    return render_template('results.html', data=food_data)
