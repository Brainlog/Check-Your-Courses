import requests
from bs4 import BeautifulSoup
import re
import json
import warnings
warnings.filterwarnings("ignore")

# Send an HTTP GET request to the website
url = 'http://ldapweb.iitd.ac.in/LDAP/courses/'
response = requests.get(url, verify=False)
datadict = {}

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data using BeautifulSoup

    links = soup.find_all('a', href=lambda href: href and href.endswith('.shtml'))
    
    # Format and dump the extracted data
    for i in range(0, len(links)):
        temp = (links[i]['href'])
        temp = url + temp
        response = requests.get(temp, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        course = soup.find_all('h2')[1].text
        data = soup.find_all('td', align = 'LEFT')
        for j in range(0, len(data)):
            if data[j].text not in datadict:
                datadict[data[j].text] = [course]
            else:
                datadict[data[j].text].append(course)
    fileptr = open('data.json', 'w')
    json.dump(datadict, fileptr)
    print(f"Retrieved data of {len(links)} courses and {len(datadict)} people")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")