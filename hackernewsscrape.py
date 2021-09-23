import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_posts(news_list):
    return sorted(news_list, key=lambda x:x['num_votes'], reverse=True)

def create_news(links, subtext):
    news = []
    for i, item in enumerate(links):
        title = item.getText
        href = item.get('href', None)
        num_votes = subtext[i].select('.score')
        if len(num_votes):
            num_votes = int(num_votes[0].getText().replace(' points', ''))
            if num_votes > 99:
                news.append({"title": title, "link": href, 'num_votes': num_votes})
    return sort_posts(news)

pprint.pprint(create_news(links, subtext))