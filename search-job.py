from bs4 import BeautifulSoup as bs

import requests as rq
import datetime

file_path = 'input/urls.txt'
compare_string = 'Beautiful'


def get_urls(path):
    """gets the urls from the file"""
    with open(path) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def extract_words(html_doc):
    """returns a list of lines"""
    # list of each word
    words = bs(html_doc, 'html.parser').get_text().replace('\n', ' ').strip().split(' ')
    # lines = bs(html_doc, 'html.parser').get_text().strip().split('\n')
    # for line in lines:
    #     line.replace('\n', ' ').replace('\r', '')
    # words = lines.split('\n')
    return words

    #return bs(html_doc, 'html.parser').get_text().strip('\n').split(" ")


def generate(compare, words, url):
    sentence = []
    print('the word to compare: ', compare)
    for i in range(len(words)):
        if words[i] == compare:
            sentence = words[i-5:i+5]
            url = url
            return '{} : {}'.format(sentence, url)


def process(urls):
    count = 0
    for url in urls:
        count += 1
        url = url
        raw = rq.get(url).text
        words = extract_words(raw)
        statement = generate(compare_string, words, url)
        print('url {} : {} '.format(count, statement))

    #return '{} : {}'.format(statement[0], statement[1])


def run():
    # returns list of urls
    urls = get_urls(file_path)
    process(urls)


run()

