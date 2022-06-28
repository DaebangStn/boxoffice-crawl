import csv

from request_html import request_html
from parser import parse_html

if __name__ == '__main__':
    f = open('boxoffice.csv', 'w', newline='')
    wr = csv.writer(f)

    for year in range(2004, 2022):
        for month in range(1, 13):
            date = 'year {}, month {}'.format(year, month)
            wr.writerow([date])
            page = request_html(monthFrom=month, yearFrom=year)
            data = parse_html(page)
            wr.writerow(data)
            print('month {}, year {} added'.format(month, year))

    f.close()
