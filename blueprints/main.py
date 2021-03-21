from flask import Flask, Blueprint, render_template, request
from urllib.parse import quote
from urllib.request import urlopen
import json

main = Blueprint('main', __name__)

AIR_VISUAL_URL = "http://api.airvisual.com/v2/nearest_city?key=cca9802f-7691-4bc6-ad75-fe583f6009ae"

@main.route("/")
def index():
    air = get_nearest()

    return render_template("main.html" , air = air)

def get_nearest():

    url = AIR_VISUAL_URL.format()

    data = urlopen(url).read()

    parsed = json.loads(data)

    air = None
    if parsed.get('air'):

        country = parsed['data']['country']

        air = {'country': country}

    return air