from flask import Flask
from main import main
from search import search
from about import about

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(search)
app.register_blueprint(about)

app.env="development"
app.run(debug=True)
