'''
Author: yanxiao333 yanxiao_333@126.com
Date: 2023-05-30 21:19:06
LastEditors: yanxiao333 yanxiao_333@126.com
LastEditTime: 2023-06-04 09:03:01
FilePath: \python-js-study-two\520-test\5_30_demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests

headers = {
    'authority':
    'pagead2.googlesyndication.com',
    'accept':
    '*/*',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'origin':
    'https://movie.douban.com',
    'referer':
    'https://movie.douban.com/top250',
    'sec-ch-ua':
    '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'cross-site',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-client-data':
    'CLC1yQEIiLbJAQijtskBCKmdygEIhIPLAQiSocsBCK2czQEIhaDNAQi2qs0BGIynzQE=',
}

params = {
    'sv': '200',
    'tid': 'gda',
    'tv': 'r20230531',
    'st': 'env',
}

response = requests.get(
    'https://pagead2.googlesyndication.com/getconfig/sodar',
    params=params,
    headers=headers).json()['bg_binary']
print(response)
