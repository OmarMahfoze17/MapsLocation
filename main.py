import sys
import urllib

googleGeocodeUrl = 'http://maps.google.com/maps/geo?'

def geocode(address):
    parms = {
        'output': 'csv',
        'q': address}

    url = googleGeocodeUrl + urllib.urlencode(parms)
    resp = urllib.urlopen(url)
    resplist = list(resp)
    line = resplist[0]
    status, accuracy, latitude, longitude = line.split(',')
    return latitude, longitude

def main():
    if 1 < len(sys.argv):
        address = sys.argv[1]
    else:
        address = '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA'

    coordinates = geocode(address)
    print coordinates

if __name__ ==  '__main__':
    main()
