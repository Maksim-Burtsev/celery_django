import requests
from bs4 import BeautifulSoup



def parse_article_data(link:str) -> tuple[str, str]:
    response = requests.get(link)   
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        h1 = soup.find('h1')
        span = soup.find_all('span', {'class': 'tm-icon-counter__value'})

        name = h1.text
        views = span[0].text

    else:
        name = 'Страница не найдена'
        views = '-'
    
    return name, views