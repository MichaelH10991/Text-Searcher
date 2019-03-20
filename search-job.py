#from bs4 import beautifulsoup
import requests as rq

url = 'https://www.crummy.com/software/BeautifulSoup/'

r = rq.get(url)

print(r.text)
