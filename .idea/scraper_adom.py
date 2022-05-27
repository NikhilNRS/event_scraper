import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


def get_event_data(url):
    response = requests.get(url)
    text = response.text
    data = BeautifulSoup(text, 'html.parser')

    # get event locations
    event_locations = data.find_all(class_="eventplace")
    event_locations_list = []
    for x in event_locations:
        event_locations_list.append(x.text)

    # get event dates
    event_dates = data.find_all(class_="date")
    event_dates_list = []
    for x in event_dates:
        event_dates_list.append(x.text)

    # get event titles
    event_titles = data.find_all(class_="eventtitle")
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
url_june = 'https://www.evenementkalender.nl/2022-06'

may_data = get_event_data(url_may)
june_data = get_event_data(url_june)

print(may_data)
print(june_data)

