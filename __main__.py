import pandas as pd
from daftlistings import Daft, Location, SearchType, PropertyType, SortType, MapVisualization
from scripts import add_time, add_distance, coord_finder, map_gen, move_file, open_html, run_input_form, actual_time, read_json
import webbrowser
import datetime

#input form take data from the user with the option of save data for future use
result = run_input_form()

destination = result['address']
max_distance = int(result['max_distance'])
min_price = int(result['min_price'])
max_price = int(result['max_price'])
beds_number = int(result['beds_number'])

if result['use_actual_date'] == 'Yes' :
    research_date = actual_time()
else :
    research_date = result['date']

daft = Daft()
daft.set_location(Location.DUBLIN) 
daft.set_search_type(SearchType.RESIDENTIAL_RENT)
daft.set_sort_type(SortType.PRICE_ASC)
daft.set_min_price(min_price)
daft.set_max_price(max_price)
daft.set_min_beds(beds_number)
daft.set_max_beds(beds_number)

listings = daft.search()

# cache the listings in the local file  
with open("result.txt", "w") as fp:
  fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

# read from the local file
with open("result.txt") as fp:
  lines = fp.readlines()

properties = []
for line in lines:
  properties.append(eval(line))

df = pd.DataFrame(properties)

#I add some extra filter on dataframe since i notice daftlisting filter doesnt work properly(at lest in my test)

#filter for beds number value 
beds_filter1 = str(beds_number) + ' bed'
beds_filter2 = str(beds_number) + ' Bed'
df = df.loc[df['bedrooms'].isin([beds_filter1 , beds_filter2])]

#filter for price lower than
df = df.loc[df['monthly_price'] < max_price  ]

#research coord from destination address
destination_coord = coord_finder(destination)

#add distance from destination column in the dataframe
add_distance(destination_coord,df)

#filter for distance lower than
df = df.loc[df['distance'] < max_distance ]

#add time column
if result['use_google_maps_api'] == 'Yes' :
    api_maps = read_json('api','api_maps.json','api_maps')
    add_time(destination,df,result['use_google_maps_api'],research_date,api_maps)
else :
    add_time(destination,df,result['use_google_maps_api'],research_date,' ')

#print(df)

dublin_map = map_gen(df)
dublin_map.add_markers()
dublin_map.add_colorbar()
dublin_map.save("ireland_rent.html")

move_file(" ","\outputs","result.txt")
move_file(" ","\outputs","ireland_rent.html")

if result['open_browser'] == 'Yes' :
  open_html("outputs", "ireland_rent.html")

print("Done, please checkout the html file")


