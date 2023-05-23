#!C:/Users/凡人/AppData/Local/Programs/Python/Python39/Python.exe
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: E:\vscode_items\python-js-study-two\520-test\demo_523.py
# DATE: 2023/05/23 周二
# TIME: 14:32:06

# DESCRIPTION:
from requests_html import HTMLSession
from copyheaders import headers_raw_to_dict

session = HTMLSession()
str = '''

'''
url = ''
headers = headers_raw_to_dict(str)


def main():
    get_data_one()
    pass


if __name__ == '__main__':
    main()