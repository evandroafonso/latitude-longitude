import pandas as pd
import requests
import json

dataFrame = pd.read_csv("Sales_January_2019.csv")

for i, row in dataFrame.iterrows():
    getAddress = str(dataFrame.at[i, 'Purchase Address'])

    parameters = {
        "key": "your key",
        "location": getAddress
    }

    response = requests.get(
        "http://www.mapquestapi.com/geocoding/v1/address", params = parameters)

    data = json.loads(response.text)['results']

    latitude = data[0]['locations'][0]['latLng']['lat']
    longitude = data[0]['locations'][0]['latLng']['lng']

    dataFrame.at[i, 'lat'] = latitude
    dataFrame.at[i, 'lng'] = longitude

dataFrame.to_csv('sales_january.csv')
