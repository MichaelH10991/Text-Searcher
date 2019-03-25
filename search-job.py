from bs4 import BeautifulSoup as bs
from urllib.parse import urlsplit

import requests as rq
import datetime

file_path = 'input/urls.txt'
happy = 'resources/happy_words.txt'
sad = 'resources/sad_words.txt'
compare_string = ''

print('the word to compare: \"{}\"'.format(compare_string))


def get_urls(path):
    """gets the urls from the file"""
    with open(path) as f:
        content = f.readlines()
    return [x.strip() for x in content]


happy_array = get_urls(happy)
sad_array = get_urls(sad)


def extract_words(html_doc):
    """returns a list of lines"""
    # list of each word
    return bs(html_doc.text, 'html.parser').get_text().lower().replace('\n', ' ').strip().split(' ')


def generate(compare, words):
    """returns a list of found words with the 10 words either side"""
    sentences = []
    for i in range(len(words)):
        if words[i] == compare:
            sentence = words[i-10:i+10]
            sentences.append(sentence)
    return sentences


def mood(happy, sad, words):
    """I dunno if this works lol but it should compute occurences of each word in the array provided"""
    happy_word_matches = 0
    sad_word_matches = 0

    for i in range(len(happy)):
        for word in words:
            if word == happy[i]:
                happy_word_matches += 1

    for i in range(len(sad)):
        for word in words:
            if word == sad[i]:
                sad_word_matches += 1

    return [happy_word_matches, sad_word_matches]


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


def calculate_mood(url):
    happy_ratio = 0
    sad_ratio = 0

    raw = rq.get(url)
    print("status code: {}".format(raw.status_code))
    words = extract_words(raw)
    mood_items = mood(happy_array, sad_array, words)
    happy_words = mood_items[0]
    sad_words = mood_items[1]
    print('{} has {} matches of happy words and {} matches of sad words'.format(url, happy_words,
                                                                                    sad_words))
    try:
        if not happy_words == 0 or not sad_words == 0:
            happy_ratio = happy_words / (happy_words + sad_words)
            sad_ratio = sad_words / (happy_words + sad_words)
            print('happy words {}%'.format(happy_ratio))
            print('sad words {}%'.format(sad_ratio))
    except ZeroDivisionError:
        print('there is a 0 somewhere')

    if happy_ratio > sad_ratio:
        print('this is a happy site')
    elif happy_ratio < sad_ratio:
        print('this is a sad website')
    else:
        print('this is a neutral website')


def run():
    # returns list of urls
    urls = get_urls(file_path)

    for url in urls:

        calculate_mood(url)
        print("=============================================================================")

    #process(urls)


run()

