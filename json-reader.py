import json
from pprint import pprint


def test():
    with open('assets/countrycode-latlong-array.json') as f:
        data = json.load(f)

    pprint(data)

def get_lat_long(country_code):

    with open('assets/countrycode-latlong-array.json') as f:
        data = json.load(f)

    return data[country_code][0], data[country_code][1]

def get_country_code(country):

    with open('assets/countries.json') as f:
        data = json.load(f)

    #print(data['country_codes'])

    codes = data['country_codes']

    for item in codes:
        #print(item)

        if(item['name'].lower() == country):
            return item['code']

    #return codes[country_code]    

#test()

#
#print(lat_long)

#country_code = get_country_code('Canada')
country_code = get_country_code('india')
#print(country_code)
lat_long = get_lat_long('ca')
print(lat_long)