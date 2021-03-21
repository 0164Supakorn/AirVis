from flask import Flask, Blueprint, render_template, request
from urllib.parse import quote
from urllib.request import urlopen
import json

search_uk = Blueprint('search_uk', __name__)

uk_city = "http://api.airvisual.com/v2/city?city={0}&state=england&country=United%20Kingdom&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"
uk_city_list = "http://api.airvisual.com/v2/cities?state=england&country={0}&key=cca9802f-7691-4bc6-ad75-fe583f6009ae"

@search_uk.route('/search_uk')
def uksearchpage():
    city = request.args.get('city')
    if not city:
        city = 'london'
    uk = 'United Kingdom'
    data = get_uk(city)
    data_list = get_uk_list(uk)
    return render_template("search_uk.html", data=data, data_list=data_list)

def get_uk(city):
    try:
        query = quote(city)
        url = uk_city.format(query)
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
        data = {'city': "Not found",
                'tp': "Not found",
                'aqius': "Not found"}
        return data

def get_uk_list(uk):
    try:
        query = quote(uk)
        url = uk_city_list.format(query)
        data = urlopen(url).read()
        parsed = json.loads(data)
        data = []
        if parsed.get('data'):
            for i in range(166):
                state = parsed['data'][i]['city']
                data.append(state)
        return data
    except:
        return data
