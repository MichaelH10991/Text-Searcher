from bs4 import BeautifulSoup
import requests as rq

file_path = 'input/urls.txt'


def get_urls(path):
    """gets the urls from the file"""
    with open(path) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def process(urls):
    """gets the raw html data from the request"""
    data = [rq.get(url).text for url in urls]
    return data


def run():
    urls = get_urls(file_path)
    print(urls)
    htmls = process(urls)
    for html in htmls:
        print(html)


run()

