from bs4 import BeautifulSoup
import requests
from datetime import date
from Categories1 import Categories1, url


def web_name():
    topic = Categories1().name_change()
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content, 'html.parser')
    try:
        website_name = soup.select('head > title')[0].text
        website_name = website_name.replace("'", "''")
        print(topic, url, website_name)
        return topic, url, website_name
    except IndexError:
        website_name = ""
        return topic, url, website_name

def today_date():

    today = date.today()
    print("Today's date:", today)
    return str(today)
