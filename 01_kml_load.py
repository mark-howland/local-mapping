

import geopandas as gpd
from shapely.geometry import Point, Polygon
import pandas as pd
import matplotlib.pyplot as plt
import folium


gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
my_map = gpd.read_file('StAlbans_final_proposals.kml', driver='KML')
my_map

type(my_map)


print(my_map)
my_map.plot()
plt.show()

locations = pd.read_csv('lat_long_dataset.csv')
locations


geometric_points = []
for xy in zip(locations['longitude'], locations['latitude']):
   geometric_points.append(Point(xy))
   
   
   
geo_locations = gpd.GeoDataFrame(locations,
                                 crs = {'init': 'epsg:4326'},
                                 geometry = geometric_points)
geo_locations




print(my_map)
my_map.plot()
geo_locations.plot()
plt.show()





### ward map

plt.style.use("seaborn-poster")
my_map.plot()
plt.title("St Albans District Council Wards")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.tight_layout()
plt.show()


## ward names

fig, ax = plt.subplots()
ax.scatter(locations['longitude'], locations['latitude'], color = "yellow", s = 700, alpha = 0.5)

for i, txt in enumerate(locations['Ward']):
    ax.annotate(txt, (locations['longitude'][i], locations['latitude'][i]))
plt.show()







####  https://medium.com/nerd-for-tech/labelling-areas-of-coordinates-with-geopandas-74d25c8aada6


my_map['coords'] = my_map['geometry'].apply(lambda x: x.representative_point().coords[:])
my_map['coords'] = [coords[0] for coords in my_map['coords']]
fig, ax = plt.subplots(figsize = (10,10))
my_map.plot(ax=ax, color='yellow', edgecolor='black')
for idx, row in my_map.iterrows():
   plt.annotate(text=row['Name'], xy=row['coords'], horizontalalignment='center', color='blue' )
plt.show()









plt.style.use("seaborn-poster")
my_map['coords'] = my_map['geometry'].apply(lambda x: x.representative_point().coords[:])
my_map['coords'] = [coords[0] for coords in my_map['coords']]
fig, ax = plt.subplots(figsize = (10,10))
my_map.plot(ax=ax, color='yellow', edgecolor='black')
for idx, row in my_map.iterrows():
   plt.annotate(text=row['Name'], xy=row['coords'], horizontalalignment='center' , fontsize = 8)
plt.title("St Albans District Council Wards")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.tight_layout()   
plt.show()





plt.style.use("seaborn-poster")
my_map['coords'] = my_map['geometry'].apply(lambda x: x.representative_point().coords[:])
my_map['coords'] = [coords[0] for coords in my_map['coords']]
fig, ax = plt.subplots(figsize = (10,10))
my_map.plot(ax=ax, color='yellow', edgecolor='black')
for idx, row in my_map.iterrows():
   plt.annotate(text=row['Name'], xy=row['coords'], horizontalalignment='center' , fontsize = 8)
plt.title("St Albans District Council Wards")
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.tight_layout()   
plt.show()






plt.style.use("seaborn-poster")
my_map['coords'] = my_map['geometry'].apply(lambda x: x.representative_point().coords[:])
my_map['coords'] = [coords[0] for coords in my_map['coords']]
fig, ax = plt.subplots(figsize = (10,10))
my_map.plot(ax=ax, color='yellow', edgecolor='black')
for idx, row in my_map.iterrows():
   plt.annotate(text=row['Name'], xy=row['coords'], horizontalalignment='center' , fontsize = 8)
plt.title("St Albans District Council Wards")
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.tight_layout()   
plt.show()



### add 3 letter ward name to geo df


my_map3 = pd.merge(my_map, locations, how = 'left', left_index = True, right_index =True)



my_map['coords'] = my_map['geometry'].apply(lambda x: x.representative_point().coords[:])
my_map['coords'] = [coords[0] for coords in my_map['coords']]
fig, ax = plt.subplots(figsize = (15,15))
my_map.plot(ax=ax, color='yellow', edgecolor='black', linewidth=2,  markersize=0)
for idx, row in my_map3.iterrows():
   plt.annotate(text=row['ward'], xy=row['coords'], horizontalalignment='center', verticalalignment ='center' , fontsize = 14)
plt.title("St Albans District Council Wards", fontsize = 30)
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.tight_layout()   
plt.show()


###




my_map['coords'] = my_map['geometry'].apply(lambda x: x.representative_point().coords[:])
my_map['coords'] = [coords[0] for coords in my_map['coords']]
fig, ax = plt.subplots(figsize = (15,15))
my_map.plot(ax=ax, color=my_map3['colortest'], edgecolor='black', linewidth=2,  markersize=0)
for idx, row in my_map3.iterrows():
   plt.annotate(text=row['ward'], xy=row['coords'], horizontalalignment='center', verticalalignment ='center' , fontsize = 14)
plt.title("St Albans District Council Wards", fontsize = 30)
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.tight_layout()   
plt.show()

