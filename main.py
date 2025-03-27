import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import brazilcep

file_path = "BD_MAPAMB.xlsx" 
sheet_name = "Consulta1" 
df = pd.read_excel(file_path, sheet_name=sheet_name)
print(df.head())

if 'CEP' not in df.columns or 'CLIENTE' not in df.columns:
    raise ValueError("As colunas 'CEP' e 'Cliente' são obrigatórias no arquivo Excel.")


geolocator = Nominatim(user_agent="LM")

df = df.iloc[:,:]
def get_coordinates(cep):
    try:
        endereco = brazilcep.get_address_from_cep(str(cep))
        location = geolocator.geocode(f"{endereco["street"]}, {endereco["district"]}, {endereco["city"]}, {endereco["uf"]}, Brasil")
        if location:
            return location.latitude, location.longitude
        return None, None
    except GeocoderTimedOut:
        return None, None


mapa = folium.Map(location=[-15.8267, -47.9218], zoom_start=5)


for _, row in df.iterrows():
    lat, lon = get_coordinates(row['CEP'])
    print("Adicionando cliente:", row['CLIENTE'] , "Lat:", lat, "Lon:", lon)
    if lat and lon:
        popup_info = "<b>CLIENTE:</b> {}<br>".format(row['CLIENTE'])
        for col in df.columns:
            if col not in ['CEP', 'CLIENTE']:
                popup_info += "<b>{}:</b> {}<br>".format(col, row[col])
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_info, max_width=300),
            tooltip=row['CLIENTE'],
            icon=folium.Icon(color='blue')
        ).add_to(mapa)

mapa.save("mapa_clientes.html")
print("Mapa gerado com sucesso: mapa_clientes.html")
