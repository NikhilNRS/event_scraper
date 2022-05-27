import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.evenementkalender.nl/2022-05'
response = requests.get(url)
text = response.text
data = BeautifulSoup(text, 'html.parser')
# print(data)

headings = data.find_all('li')
print(headings)

# headings = data.find_all('tr')[0]
# headings_list = []  # list to store all headings
#
# for x in headings:
#     headings_list.append(x.text)
#
# print(headings_list[:10])
