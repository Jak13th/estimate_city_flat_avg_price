import requests
from bs4 import BeautifulSoup
import re
from math import sqrt

def get_superficie(ville):

    response = requests.get(
        url=f"https://fr.wikipedia.org/wiki/{ville}",
    )

    # Request wikipedia worked if status code == 200
    print("Status code : ",  response.status_code)

    # Initiate beautifulsoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # look for information table contening city's 'superficie' info
    table = soup.find('table', {"class":"infobox_v2 noarchive"})

    # Build a dict in order to have information under format key:value :
    dict_for_table = {}
    for element in table.find_all('tr'):
        if element.find('th')!=None and element.find('td')!=None:
            dict_for_table[element.find('th').text.strip()]=element.find('td').text.strip()

    result = re.match(r"^(\d*)", dict_for_table['Superficie']).group(0)

    return int(sqrt(int(result))*1000)

# Test
if __name__=='__main__':
    print((get_superficie('Paris')))