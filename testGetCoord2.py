
#from geopy.geocoders import Nominatim
#from geopy.geocoders import GoogleV3
import math
from geopy.geocoders import GoogleV3

R = 6371e3
PI=math.pi
def getLocation(address):
    gmaps = GoogleV3('AIzaSyAnRmqg-kRi7wBE_v1wkujL12RqQV2dGIA')
#address = 'Arab ElRamel Quesna Monofiay Egypt'
    googleAddress, latLng  = gmaps.geocode(address)
#    print googleAddress, latLng 
    return googleAddress, latLng 

def getDistance(address_1, address_2):
    googleAddress, latLng_1 = getLocation(address_1)
    googleAddress, latLng_2 = getLocation(address_2)
    a=math.sin(math.radians(latLng_2[0]-latLng_1[0])/2)**2+math.cos(math.radians(latLng_2[0]))*math.cos(math.radians(latLng_1[0]))*math.sin(math.radians(latLng_2[1]-latLng_1[1])/2)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    d=R*c
    return d
    


def main():
    address_1 = 'Arab ElRamel Quesna Monofiay Egypt'
    address_2 = 'W6 8NB, London'
    googleAddress, latLng = getLocation(address_1)
    print googleAddress, latLng
    googleAddress, latLng = getLocation(address_2)
    print googleAddress, latLng

    distance=getDistance(address_1,address_2)
    
    print 'The distance between ',address_1,'and',address_2,' is ',distance/1000, 'km'



if __name__ ==  '__main__':
    main()


#print lng[0],lng[1]
#latitude_1=lng[0]
#longitude_1=lng[1]
#latitude_2=51.4863143
#longitude_2=-0.2180049
#d_lat=latitude_2-latitude_1
#d_lng=longitude_2-longitude_1
#a=math.sin(math.radians(d_lat)/2)**2+math.cos(math.radians(latitude_2))*math.cos(math.radians(latitude_1))*math.sin(math.radians(d_lng)/2)**2
#c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
#d=R*c
#print 'Distabce between the tow points is ',d/1000,'KM'




#googleGeocodeUrl = 'http://maps.google.com/maps/geo?'

#def geocode(address):
#    parms = {
#        'output': 'csv',
#        'q': address}

#    url = googleGeocodeUrl + urllib.urlencode(parms)
#    resp = urllib.urlopen(url)
#    resplist = list(resp)
#    line = resplist[0]
#    status, accuracy, latitude, longitude = line.split(',')
#    return latitude, longitude

#def main():
# 
#    address = '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA'
#    print address
#    coordinates = geocode(address)
#    print coordinates


