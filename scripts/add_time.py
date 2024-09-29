
from .time_calc import *

def add_time(destination,df,api_call,research_date,api_maps):
  travelTime = []
  for index, row in df.iterrows():
    if api_call == 'Yes' :
        T1 = time_calc(row['latitude'], row['longitude'], destination, research_date, api_maps)
    else :
        T1 = 'n/a'
    travelTime.append(T1)
  df["traveltime"] = travelTime 

