from flask import Flask, Blueprint, render_template, request
from urllib.parse import quote
from urllib.request import urlopen
import json

search_th = Blueprint('search_th', __name__)

bangkok_city = "http://api.airvisual.com/v2/city?city={0}&state={0}&country=thailand&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"
bangkok_city_list = "http://api.airvisual.com/v2/states?country={0}&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"

@search_th.route('/search_th')
def searchpage():
    state = request.args.get('state')
    if not state:
        state = 'bangkok'
    thailand = 'thailand'
    data = get_bangkok(state)
    data_list = get_bangkok_list(thailand)
    return render_template("search_th.html", data=data, data_list=data_list)

def get_bangkok(state):
    try:
        query = quote(state)
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
            icon = parsed['data']['current']['weather']['ic']
            url_icon = f"https://www.airvisual.com/images/{icon}.png"
            data = {'city': city,
                'state': state,
                'country': country,
                'aqius': aqius,
                'tp': tp,
                'url_icon':url_icon
                }
        return data
    except:
        data = {'state': "Not found",
                'tp': "Not found",
                'aqius': "Not found"}
        return data

def get_bangkok_list(thailand):
    try:
        query = quote(thailand)
        url = bangkok_city_list.format(query)
        data = urlopen(url).read()
        parsed = json.loads(data)
        data = []
        if parsed.get('data'):
            for i in range(42):
                state = parsed['data'][i]['state']
                data.append(state)
        return data
    except:
        return data
