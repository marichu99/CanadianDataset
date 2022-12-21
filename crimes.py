import pandas as pd
import folium
import requests
import io

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv"

df_crimes=pd.read_csv(url)
print(df_crimes.head())
# check the shape of the dataframe
print(df_crimes.shape)
# lets filter to the first 100 crimes
df_incidents=df_crimes.loc[:100,:]
print(df_incidents.shape)

# print the map of san fransisco and visualize it
san_fran_map= folium.Map(
    location=[37.77,-122.42],
    zoom_start=12   
)
# add markers to hotspots and visualize it
for lat,lng in zip(df_incidents.X,df_incidents.Y):
    san_fran_map.add_child(
        folium.CircleMarker(
            location=[lat,lng],
            radius=5,
            color="red",
            fill_color="red"
        )

    )
san_fran_map.show_in_browser()