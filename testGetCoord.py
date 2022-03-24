#from geopy.geocoders import Nominatim
#from geopy.geocoders import GoogleV3
import math
from geopy.geocoders import GoogleV3

R = 6371e3
PI=math.pi
gmaps = GoogleV3('AIzaSyAnRmqg-kRi7wBE_v1wkujL12RqQV2dGIA')
address = 'Arab ElRamel Quesna Monofiay Egypt'
lat, lng = gmaps.geocode(address)
print lat, lng

print lng[0],lng[1]
latitude_1=lng[0]
longitude_1=lng[1]
latitude_2=51.4863143
longitude_2=-0.2180049
d_lat=latitude_2-latitude_1
d_lng=longitude_2-longitude_1
a=math.sin(math.radians(d_lat)/2)**2+math.cos(math.radians(latitude_2))*math.cos(math.radians(latitude_1))*math.sin(math.radians(d_lng)/2)**2
c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
d=R*c
print 'Distabce between the tow points is ',d/1000,'KM'

