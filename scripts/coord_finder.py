from geopy.geocoders import Nominatim

def coord_finder(destination):
    geolocator = Nominatim(user_agent="my_request")
    destination_coord = geolocator.geocode(destination)
    return destination_coord