from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    country  = request.form.get('country')

    country_code = get_country_code(country)
    lat, long = get_lat_long(country_code)
    
    result = {
        'country' : country,
        'code' : country_code,
        'lat': lat,
        'long' : long
    }
    
    #return content
    return render_template('result.html', result=result)

def get_country_code(country):

    with open('assets/countries.json') as f:
        data = json.load(f)

    #print(data['country_codes'])

    codes = data['country_codes']

    for item in codes:
        #print(item)

        if(item['name'].lower() == country):
            return item['code'].lower()

    #return codes[country_code]      

def get_lat_long(country_code):

    with open('assets/countrycode-latlong-array.json') as f:
        data = json.load(f)

    return data[country_code][0], data[country_code][1]    

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
    
    https://www.learnpython.org/en/String_Formatting
    
    https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    
    https://github.com/googlemaps/google-maps-services-python
    
    AIzaSyCRhRz_mw_5wIGgF-I6PUy3js6dcY6zQ6Q
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''