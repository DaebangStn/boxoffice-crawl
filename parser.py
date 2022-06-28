from bs4 import BeautifulSoup as bs


def parse_html(html):
    soup = bs(html, "html.parser")
    rows = soup.find('tbody').find_all('tr')

    for row in rows:
        print(row)

