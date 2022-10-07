import requests
from scrapper_wiki import get_superficie

token = "pk.eyJ1IjoiamFrMTN0aCIsImEiOiJja3pta3B6d3IycWJxMnZvYzVnNmh1cGZjIn0.0wGgN1yfP59SvOMUsrvhOA"

def get_price(lat, lon, dist):
    List_price = []
    response = requests.get(f"http://api.cquest.org/dvf?lat={lat}&lon={lon}&dist={dist}")
    data = response.json()
    for elem in data["features"]:
        if "type_local" in elem["properties"]:
            if elem["properties"]['type_local']=="Appartement":
                if "valeur_fonciere" in elem["properties"]:
                    List_price.append(elem["properties"]["valeur_fonciere"])

    
    average_price = sum(List_price)/len(List_price)
    print("Le prix moyen des biens immobiliers dans cette zone est de: ", average_price)

def get_geocoded_position(ville):
    response = requests.get(f"https://api.mapbox.com/geocoding/v5/mapbox.places/{ville}.json?access_token={token}", verify=False)
    data_geopos = response.json()
    return data_geopos["features"][0]["center"]

if __name__=="__main__":
    ville = "Belfort" #input("Entrez une ville : ")
    coordinates = get_geocoded_position(ville)
    print(coordinates)
    latitude = coordinates[1] #input("Entrez la latitude: ")
    longitude = coordinates[0] #input("Entrez la longitude: ")
    get_price(latitude, longitude, get_superficie(ville=ville))
