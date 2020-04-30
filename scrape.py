from pprint import pprint

import requests
from bs4 import BeautifulSoup


def create_custom_news(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'href': href, 'points': points})
    return sorted(hn, key=lambda k: k['points'], reverse=True)


def main():
    response = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    pprint(create_custom_news(links, subtext))


if __name__ == '__main__':
    main()
