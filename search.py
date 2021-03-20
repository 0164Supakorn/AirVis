from flask import Flask, Blueprint, render_template, request, jsonify
from urllib.parse import quote
from urllib.request import urlopen
import json

search = Blueprint('search', __name__)

bangkok_city = "http://api.airvisual.com/v2/city?city={0}&state=bangkok&country=thailand&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"
bangkok_city_list = "http://api.airvisual.com/v2/cities?state={0}&country=thailand&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"

@search.route('/search')
def searchpage():
    city = request.args.get('city')
    if not city:
        city = 'bangkok'
    bangkok = 'bangkok'
    data = get_bangkok(city)
    data_list = get_bangkok_list(bangkok)
    return render_template("search.html", data=data, data_list=data_list)

def get_bangkok(city):
    try:
        query = quote(city)
        url = bangkok_city.format(query)
        data = urlopen(url).read()
        parsed = json.loads(data)
        data = None

        if parsed.get('data'):

            city = parsed['data']['city']
            state = parsed['data']['state']
            country = parsed['data']['country']
            aqius = parsed['data']['current']['pollution']['aqius']
            tp = parsed['data']['current']['weather']['tp']
            data = {'city': city,
                'state': state,
                'country': country,
                'aqius': aqius,
                'tp': tp
                }
        return data
    except:
        data = {'city': "Not found",
                'tp': "Not found",
                'aqius': "Not found"}
        return data

def get_bangkok_list(bangkok):
    try:
        query = quote(bangkok)
        url = bangkok_city_list.format(query)
        data = urlopen(url).read()
        parsed = json.loads(data)
        data = []
        if parsed.get('data'):
            for i in range(42):
                city = parsed['data'][i]['city']
                data.append(city)
        return data
    except:
        data = {'city': "City not found"}
        return data
