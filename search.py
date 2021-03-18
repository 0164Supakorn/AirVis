from flask import Flask, Blueprint, render_template, request
from urllib.parse import quote
from urllib.request import urlopen
import json

search = Blueprint('search', __name__)

AIR_VISUAL_URL = "http://api.airvisual.com/v2/city?city={0}&state={1}&country={2}&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"

@search.route('/search')
def searchpage():
    city = request.args.get('city')
    state = request.args.get('state')
    country = request.args.get('country')
    if not city:
        city = 'bangkok'
        state = 'bangkok'
        country = 'thailand'

    air = get_air(city, state, country)

    return render_template("search.html" , air=air)

def get_air(city, state, country):
    try:
        query = quote(city, state, country)
        url = AIR_VISUAL_URL.format(query)
        data = urlopen(url).read()
        parsed = json.loads(data)
        air = None

        if parsed.get('air'):

            city = parsed['data']['city']
            state = parsed['data']['state']
            country = parsed['data']['country']
            air = {'city': city,
                'state': state,
                'country': country
                }
        return air
    except:
        air = None
        return air