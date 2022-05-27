import requests
from bs4 import BeautifulSoup
import time
from itertools import islice
import pandas as pd

def read_file():
    with open('body.txt') as f:
        lines = f.readlines()
    return lines

def find_body(url):
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
                

def get_event_data(body):

    body = BeautifulSoup(open("body.txt").read())

    # get event locations
    event_locations = body.find_all(class_="eventplace")
    event_locations_list = []
    for x in event_locations:
        event_locations_list.append(x.text)

    # get event dates
    event_dates = body.find_all(class_="date")
    event_dates_list = []
    for x in event_dates:
        event_dates_list.append(x.text)

    # get event titles
    event_titles = body.find_all(class_="eventtitle")
    event_titles_list = []
    for x in event_titles:
        event_titles_list.append(x.text)

    # combine lists
    df = pd.DataFrame(list(zip(event_titles_list, event_dates_list, event_locations_list)),
                      columns =['Title', 'Date', 'Location'])
    df.columns = df.iloc[0]
    df.drop(index=0, axis=0, inplace=True)
    return df

# run code
url_may = 'https://www.evenementkalender.nl/2022-05'

may_data = get_event_data(find_body(url_may))

print(may_data)

