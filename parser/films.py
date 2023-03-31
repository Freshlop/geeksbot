from pprint import pprint

import requests
from bs4 import BeautifulSoup
import datetime

today =str(datetime.datetime.today())[:10:]




URL =f"https://kaktus.media/?lable=8&date={today}&order=time"


HEADERS = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(

    class_="ArticleItem--data ArticleItem--data--withImage"
    )
    news = []
    for item in items:
        new = {
            'title': item.find('a', class_="ArticleItem--name").string.replace('\n', ''),
            'photo': item.find("a", class_="ArticleItem--image").find('img').get('src'),
            'link': item.find('a', class_="ArticleItem--name").get('href'),
            'time': item.find('div', class_='ArticleItem--time').string.replace('\n', '')
        }
        news.append(new)
    return news




def news_parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        html = get_html(URL)
        new = get_data(html.text)
        news.extend(new)

        return news
    else:
        raise Exception("Error in parser!")
