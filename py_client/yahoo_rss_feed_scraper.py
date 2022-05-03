import requests
from bs4 import BeautifulSoup as Soup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=&lang=en-US'

r = requests.get(url, headers=headers)

soup = Soup(r.text,'xml')
newsList = soup.find_all('item')
for el in newsList:
    print("Title:", el.title.get_text())
    print("Description:", el.description.get_text())
    print("Date:", el.pubDate.get_text())
    print("\n")