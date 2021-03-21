from flask import Flask, render_template
from blueprints.main import main
from blueprints.search_th import search_th
from blueprints.search_uk import search_uk
from blueprints.pminfo import pminfo
from flask_sqlalchemy import SQLAlchemy
from models import db,Student


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

app.register_blueprint(main)
app.register_blueprint(search_th)
app.register_blueprint(search_uk)
app.register_blueprint(pminfo)

@app.route('/about')
def about():
    student = Student.query.all()
    return render_template('about.html', student=student)


app.env="development"
app.run(debug=True)
