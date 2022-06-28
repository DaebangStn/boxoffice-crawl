import requests
import datetime

def request_html(monthFrom, yearFrom, monthTo=None, yearTo=None):
    URL = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findMonthlyBoxOfficeList.do'

    assert 2004 <= yearFrom <= datetime.datetime.now().year
    assert 1 <= monthFrom <= 12

    if monthTo is None:
        monthTo = monthFrom

    if yearTo is None:
        yearTo = yearFrom

    data = {
        'loadEnd': 0,
        'searchType': 'search',
        'sSearchYearFrom': yearFrom,
        'sSearchMonthFrom': monthFrom,
        'sSearchYearTo': yearTo,
        'sSearchMonthTo': monthTo,
    }

    res = requests.post(URL, data=data)
    res.raise_for_status()

    return res.text

