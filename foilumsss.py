import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

print(dir(folium.Marker))
html = """<h4>Volcano information:</h4>
Height: %s m
"""
print(dir(folium.__builtins__))

map = folium.Map(location=[22.58, 99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map_html_popup_simple.html")