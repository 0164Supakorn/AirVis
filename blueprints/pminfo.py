from flask import Blueprint, render_template

pminfo = Blueprint('pminfo',__name__)

@pminfo.route('/pminfo')
def pm():
    return render_template('pminfo.html')