import json
import requests


url = "https://db.carnewschina.com/suggest?q="


def download_json_and_parse_brands(prefix):
    # stahneme url + prefix

    result = []

    search = url + prefix
    response = requests.get(search)
    if response.status_code == 200:

        data = json.loads(response.content)
        
        brands = data["brands"]
        for brand in brands:
            result.append(brand["name"])

            return result

    else:
        print(response.status_code)
        return []



if __name__ == "__main__":

    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)

    # pro prefix "ni" mi to vypise Nissan a Nio