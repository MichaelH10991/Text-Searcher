from bs4 import BeautifulSoup as bs

import requests as rq
import datetime

file_path = 'input/urls.txt'
compare_string = 'crack'
print('the word to compare {}'.format(compare_string))


def get_urls(path):
    """gets the urls from the file"""
    with open(path) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def extract_words(html_doc):
    """returns a list of lines"""
    # list of each word
    return bs(html_doc, 'html.parser').get_text().lower().replace('\n', ' ').strip().split(' ')


def generate(compare, words):
    """returns a list of found words with the 10 words either side"""
    sentences = []
    for i in range(len(words)):
        if words[i] == compare:
            sentence = words[i-10:i+10]
            sentences.append(sentence)
    return sentences


def process(urls):
    """processes each by finding sentences where the word in question appears"""
    for url in urls:
        url = url
        raw = rq.get(url).text
        words = extract_words(raw)
        found_sentences = generate(compare_string, words)
        if found_sentences:
            print('{} \"{}\"\'s found in {} \n extract:{}'.format(len(found_sentences), compare_string, url, found_sentences))
        else:
            print('no \"{}\"\'s found in {}'.format(compare_string, url))


def run():
    # returns list of urls
    urls = get_urls(file_path)
    process(urls)


run()

