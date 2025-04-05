import googlemaps
import datetime, time

def time_calc(latitude,longitude,address,research_date,api_maps):
  gmaps = googlemaps.Client(key=api_maps)
  origin = (latitude, longitude)
  destination = address
  result = gmaps.distance_matrix(origin, destination)
  departure_time = (time.mktime(research_date))
  mode = 'transit'
  
  publicTransportTime= result['rows'][0]['elements'][0]['duration']['text']
  return publicTransportTime