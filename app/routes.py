
from flask import flash, redirect, url_for

from flask import Blueprint, render_template, request
from .models import get_food_data

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        flash('Please enter a search term.', 'error')
        return redirect(url_for('main.home'))
    
    # If query is provided, proceed with the original logic
    data = get_food_data(query)
    return render_template('results.html', data=data)
