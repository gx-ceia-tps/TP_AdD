import folium
import io
from PIL import Image


def save_map_to_png(filename, map):
    img_data = map._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(filename)


def get_interactive_map(coordinates):
    coord_values = [coords for coords in coordinates.values()]

    # Calcular el centroide
    mean_latitude = sum(lat for lat, lon in coord_values) / len(coord_values)
    mean_longitude = sum(lon for lat, lon in coord_values) / len(coord_values)

    # Crear el mapa centrado en el centroide
    mymap = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=4)

    # Graficar ciudades
    for city, (lat, lon) in coordinates.items():
        if lat is not None and lon is not None:
            folium.Marker([lat, lon], popup=city).add_to(mymap)
    return mymap