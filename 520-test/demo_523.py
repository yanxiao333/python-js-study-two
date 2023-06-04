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
Accept:
application/json, text/plain, */*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
zh-CN,zh;q=0.9
Referer:
https://www.xingtu.cn/creative/visitor/market/index
Sec-Ch-Ua:
"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-origin
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
# X-Csrftoken:
# FIerUNA15Wao2k7qjGtlz9ZbXwrrMHOu
# X-Login-Source:
# 1
# X-Secsdk-Csrf-Token:
# 000100000001f82c8cc8cde26aace4f757f115ca173e4645a4aee283b20f0b570bafebe7937517647989bb008550
'''
url = 'https://www.xingtu.cn/gw/api/search/spu'
headers = headers_raw_to_dict(str)
data = {
    "keyword": "",
    "order_by": "score",
    "sort_type": 2,
    "page": 1,
    "limit": 30,
    "filters": {
        "first_category_id": "200",
        "second_category_id": "20001",
        "industry_id": "1903",
        "has_material": 0,
        "project": 0
    }
}


def get_data_one():
    try:
        res = session.post(url=url, headers=headers, data=data)
        if res.status_code == 200:
            print(res.text)

    except Exception as e:
        print("Error: " + str(e))


def main():
    get_data_one()
    pass


if __name__ == '__main__':
    main()