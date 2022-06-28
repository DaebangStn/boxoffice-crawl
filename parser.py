from bs4 import BeautifulSoup as bs
import csv


def parse_html(html):
    soup = bs(html, "html.parser")
    rows = soup.find('tbody').find_all('tr')

    data = []
    for row in rows:
        data_row = []
        cols = row.find_all('td')
        for col in cols:
            data_row.append(col.text.strip())

        data.append(data_row)

    return data

