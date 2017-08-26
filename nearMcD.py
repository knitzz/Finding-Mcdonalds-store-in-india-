import folium
import requests
from re import findall
city='delhi'
temp=requests.get("http://www.mcdonaldsindia.net/"+city+"-store-locator.aspx")
data=findall("LatLng\((.*)\)",temp.text)
places=findall("title: \'(.*)\'",temp.text)
lat=[]
lng=[]
for i in data:
    lat.append(float(i.split(',')[0]))
    lng.append(float(i.split(',')[1]))
map=folium.Map(location=[lat[0],lng[0]],tiles="Stamen Terrain",zoom_start=12)
closed_stores_index=findall("<span id=\"rprStore_ctl(.*)_lblclose\"",temp.text)
closed_stores_index=[int(i) for i in closed_stores_index]
t=1
print(closed_stores_index)
for i, j,k in zip(lat,lng,places):
    fg=folium.FeatureGroup(name="my map2")
    if t in closed_stores_index:
        fg.add_child(folium.Marker(location=[i,j],popup=k+"  (closed)",icon=folium.Icon(color='red')))
    else:
        fg.add_child(folium.Marker(location=[i,j],popup=k,icon=folium.Icon(color='green')))
    map.add_child(fg)
    t=t+1
map.save('mcd.html')
