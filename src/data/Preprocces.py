#%%
# Package import
import pandas as pd
import numpy as np
import os
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim 
import pycountry_convert as pc


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# Read data frame
df = pd.read_excel(os.path.abspath('../../data/Raw/Cities.xls'), index_col=0)


#%% Add _ instead of space
df.columns = df.columns.str.replace(' ', '_')

#%% Add longitude and latitude
# Initialize empty lists
longitude = [] 
latitude = [] 
   
# function to find the coordinate of a given city  
def findGeocode(city): 
       
    # try and catch is used to overcome 
    # the exception thrown by geolocator 
    # using geocodertimedout   
    try: 
          
        # Specify the user_agent as your 
        # app name it should not be none 
        geolocator = Nominatim(user_agent="VS") 
          
        return geolocator.geocode(city) 
      
    except GeocoderTimedOut: 
          
        return findGeocode(city)     
  
# each value from city column 
# will be fetched and sent to 
# function find_geocode    
for _, row in df[["City","Country"]].iterrows():
      
    if findGeocode(row["City"]+', '+ row["Country"]) != None: 
           
        loc = findGeocode(row["City"]+', '+ row["Country"]) 
          
        # coordinates returned from  
        # function is stored into 
        # two separate list 
        latitude.append(loc.latitude) 
        longitude.append(loc.longitude) 
       
    # if coordinate for a city not 
    # found, insert "NaN" indicating  
    # missing value  
    else: 
        latitude.append(np.nan) 
        longitude.append(np.nan)

# Populate the two missing manually
latitude[102], longitude[102] = 10.156421, -67.999718
latitude[155], longitude[155] = 27.773056, -82.639999

# Add columns to data frame
df["Latitude"] = np.array(latitude)
df["Longitude"] = np.array(longitude)


df.to_csv(os.path.abspath('../../data/Processed/Cities.csv'))

print("Done")

#%% Add continen
def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

df['Continent'] = [country_to_continent(con) for con in df.Country]


#%% Return files

df.to_csv(os.path.abspath('../../data/Processed/Cities.csv'))

print("Done")

# %%
