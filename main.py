from flask import Flask, Blueprint, render_template, request
from urllib.parse import quote
from urllib.request import urlopen
import json

main = Blueprint('main', __name__)

AIR_VISUAL_URL = "http://api.airvisual.com/v2/states?country={0}&key={1}"
AIR_VISUAL_KEY = '60d51ad9-da20-447f-945a-62367f32ac40'

@main.route("/")
def index():
    country = request.args.get('country')
    air = get_air(country, AIR_VISUAL_KEY)

    return render_template("main.html" , air = air)

def get_air(country, API_KEY):
    query = quote(country)
    url = AIR_VISUAL_URL.format(country, API_KEY)
    data = urlopen(url).read()
    parsed = json.loads(data)
    air = None
    if parsed.get('air'):

        country = parsed['data']['country']

        air = {'country': country}

    return air