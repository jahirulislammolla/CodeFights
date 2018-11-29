import urllib
import json

def closestStations(stations):
    x={}
    y={}
    url = 'http://transportapi.com/v3/uk/places.json?query='
    url2="&type=train_station&app_id=18f5a8f2&app_key=102ba04e8075b4647d809d06d837a273"
    for i in stations:
        result = json.load(urllib.urlopen(url+i+url2))["member"][0]
        x[i]=[result['latitude'],result['longitude']]
    z=[]
    for i in range(len(stations)-1):
        for j in range(i+1,len(stations)):
            z+=[((x[stations[i]][0]-x[stations[j]][0])**2 + (x[stations[i]][1]-x[stations[j]][1])**2)**.5]
    return min(z)
