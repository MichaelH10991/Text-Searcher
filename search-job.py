from bs4 import BeautifulSoup as bs
from urllib.parse import urlsplit

import requests as rq
import datetime

file_path = 'input/urls.txt'
compare_string = 'hate'
happy_array = ['beautiful', 'cool']
sad_array = ['hate']
print('the word to compare: \"{}\"'.format(compare_string))


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


def mood(happy, sad, words, url):
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

    return [url, happy_word_matches, sad_word_matches]


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

        mood_items = mood(happy_array, sad_array, words, url)
        print('{} has {} matches of happy words and {} matches of sad words'.format(mood_items[0], mood_items[1],
              mood_items[2]))

        if not mood_items[1] == 0 or not mood_items[2] == 0:
            happy_ratio = (mood_items[1] + mood_items[2]) / mood_items[1]
            sad_ratio = (mood_items[1] + mood_items[2]) / mood_items[2]
            print('happy words {}%'.format(happy_ratio))
            print('sad words {}%'.format(sad_ratio))
        elif mood_items[1] > 0:
            print('happy words 100%')
        else:
            print('sad words 100%')




def run():
    # returns list of urls
    urls = get_urls(file_path)
    process(urls)

    # for url in urls:
    #     print('{}{}'.format(urlsplit(url).netloc, urlsplit(url).path))


run()

