'''
Author: yanxiao333 yanxiao_333@126.com
Date: 2023-05-21 16:49:01
LastEditors: yanxiao333 yanxiao_333@126.com
LastEditTime: 2023-05-21 17:33:08
FilePath: \python-js-study-two\520-test\521_企名片.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding:UTF-8 -*-
# AUTHOR: XiaoDong Yan
# FILE: F:\vscode\python-js-study-two\520-test\521_企名片.py
# DATE: 2023/05/21 周日
# TIME: 16:49:14

# DESCRIPTION:
import execjs
import requests
import json

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua':
    '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def main(page):
    data1 = {
        'time_interval': '',
        'tag': '',
        'tag_type': '',
        'province': '',
        'lunci': '',
        'page': page,
        'num': '20',
        'unionid': '',
    }

    response = requests.post(
        'https://vipapi.qimingpian.cn/DataList/productListVip',
        headers=headers,
        data=data1).json()
    encrypt_data = response['encrypt_data']
    with open('./js_520.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    ctxs = execjs.compile(jscode).call('s', encrypt_data)['list']
    for ctx in ctxs:
        print(ctx)


if __name__ == '__main__':
    for page in range(0, 2):
        main(page)