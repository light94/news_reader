import requests
from bs4 import BeautifulSoup

HOME_URL = 'http://forumias.com/portal/todays-newspaper/'

def Soup(markup):
    return BeautifulSoup(markup, "html5lib")


r = requests.get(HOME_URL)
soup = Soup(r.text)

archive = soup.find(id='lcp_instance_0')
last_entry = archive.contents[0]
entry_link = last_entry.contents[0].get('href')

r = requests.get(entry_link)
soup = Soup(r.text)
article_list = soup.find("div",class_='pf-content').find_all("p")
article_list = article_list[2:-2]
link_list = [article.contents[0].get('href') for article in article_list]
