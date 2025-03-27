from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import brazilcep

endereco = brazilcep.get_address_from_cep('20766200')

geolocator = Nominatim(user_agent="test")
locator = geolocator.geocode(f"{endereco["street"]}, {endereco["district"]}, {endereco["city"]}, {endereco["uf"]}")

print(locator.latitude, locator.longitude)