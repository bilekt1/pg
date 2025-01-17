import sys
import requests
from lxml import html

#https://www.zenrows.com/blog/python-html-parser

"""
program stahne url a z nej vrati vsechny nadpisy:
<h1>Hlavni nadpis</h1>
<h2>Podnadpis</h2>
<h3>Podpodnadpis</h3>
<h4>Maly nadpis</h4>
<h5>Nejmensi nadpis</h5>
"""
def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []

    response = requests.get(url)
    if response.status_code == 200:

        for i in range(5):
            root = html.fromstring(response.content)
            h1s = root.xpath(f"//h{i}")
        for h1 in h1s:
            nadpis = h1.text_content()
            nadpisy.append(nadpis)
        
    else:
        print(response.status_code)
        return []
    
    #return nadpisy


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        nadpisy = stahni_url_a_vrat_nadpisy(url)
        print(nadpisy)

    except IndexError:
        print("Špatný argument")