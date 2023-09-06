import requests
from bs4 import BeautifulSoup
import re
import json

# Send an HTTP GET request to the website
url = 'http://ldapweb.iitd.ac.in/LDAP/courses/'
response = requests.get(url)
datadict = {}
fileptr = open('data.json', 'w')

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data using BeautifulSoup

    links = soup.find_all('a', href=lambda href: href and href.endswith('.shtml'))
    # data = soup.find('a href = ')
    
    # Print the extracted data
    for i in range(0, len(links)):
        print(i)
        temp = (links[i]['href'])
        temp = url + temp
        response = requests.get(temp)
        soup = BeautifulSoup(response.text, 'html.parser')
        course = soup.find_all('h2')[1].text
        data = soup.find_all('td', align = 'LEFT')
        for j in range(0, len(data)):
            if data[j].text not in datadict:
                datadict[data[j].text] = [course]
            else:
                datadict[data[j].text].append(course)
    json.dump(datadict, fileptr)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
