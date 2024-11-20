import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
            
        for a_tag in soup.find_all('a', href = True):
                hrefs.append(a_tag['href'])
    else:
        print(f"Chyba - code: {response.status_code}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)
        
        for link in links:
            print(link)
    # osetrete potencialni chyby pomoci vetve except
    except IndexError:
        print("Nebyl zadán argument v příkazovém řádku")
    except Exception as e:
        print(f"Chyba: {e}")
