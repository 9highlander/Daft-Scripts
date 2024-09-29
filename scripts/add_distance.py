import haversine as hs
from haversine import Unit

def add_distance(destinationCoord,df):
  distance = []
  for index, row in df.iterrows():
    loc1=(row['latitude'], row['longitude'])
    loc2=(destinationCoord.latitude, destinationCoord.longitude)
    T1 = hs.haversine(loc1,loc2,unit=Unit.KILOMETERS)
    distance.append(T1)
  df["distance"] = distance

