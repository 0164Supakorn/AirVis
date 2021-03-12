from flask import Blueprint, render_template

about = Blueprint('about',__name__)

@about.route('/about')
def aboutpage():
    return render_template('about.html')