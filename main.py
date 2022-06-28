from request_html import request_html
from parser import parse_html

if __name__ == '__main__':
    page = request_html(monthFrom=3, yearFrom=2022)
    parse_html(page)