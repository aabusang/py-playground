import requests
from bs4 import BeautifulSoup

#get the data
data = requests.get('')

#load data into BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser');

#get data by looking for each tr element

data = []
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values)

#get data only where rows are marked as special
data = []
for tf in soup.find_all('tr', {'class': 'special'}):
    values = [td.text for td in tr.find_all('td')]
    data.append(values);


#get data within a specific element
data = []
div = soup.find('div', {'class': 'special_table'})
for tr in div.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values)


print(data)
              
