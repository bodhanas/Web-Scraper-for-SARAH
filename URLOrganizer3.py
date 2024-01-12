import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError
import urllib.request


def scrapping_func():

    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    url = input('Please input a URL.\n')
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()

    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        print('URL has been verified!')

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    soup.prettify()
    output = ''
    text = soup.find_all(text=True)
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        'style',
        # there may be more elements you don't want, such as "style", etc.
    ]
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output, url

