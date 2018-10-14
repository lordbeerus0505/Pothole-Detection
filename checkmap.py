
import requests
import webbrowser

GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap'


# get the latitude/longitude pairs
coordinate_pairs = ["12,77"]

# this is another way of serializing the URL
preq = requests.PreparedRequest()
preq.prepare_url(GMAPS_URL, {'size':'800x500', 'zoom':'13','markers': coordinate_pairs,'key':'AIzaSyBMJ6OmoVGaX2TLUu_GY083Kn9BiCqhKRk'})
webbrowser.open(preq.url),