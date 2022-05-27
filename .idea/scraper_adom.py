import requests
from bs4 import BeautifulSoup
import time
from itertools import islice

def find_body():
    url = 'https://www.evenementkalender.nl/2022-05'
    response = requests.get(url)
    text = response.text
    data = BeautifulSoup(text, 'html.parser')

    headings = data.find_all('li')

    with open("randomfile.txt", "w") as external_file:
        print(data, file=external_file)
        external_file.close()

    start = '<h1 class="title">Evenementen in mei 2022</h1>'
    end = '<a class="totop" href="2022-05#top" title="#">naar boven<span></span></a>'

    with open("randomfile.txt") as myFile:
        for num, line in enumerate(myFile, 1):
            if start in line:
                _start = num
    
    with open("randomfile.txt") as my2File:
        for num, line in enumerate(my2File, 1):
            if end in line:
                _end = num

    with open("randomfile.txt") as my3File:
        lines = islice(my3File, _start, _end)
        with open("body.txt", "w") as external_file:
            for line in lines:
                print(line, file=external_file)
                
find_body()



                




    