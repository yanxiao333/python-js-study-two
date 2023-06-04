import requests

cookies = {
    'Hm_lvt_5d77c979053345c4bd8db63329f818ec':
    '1685603902',
    'ttcid':
    '3e0d9411c3fd45a29c7a627c0b6f9ff947',
    'tt_scid':
    'keDLRKc9htpnkVz5WLRgHP3xLEKCL0oWWd5ZwPHbCb5cq.x7sOkxc6kg4z3OCZyi1376',
    'star_login_type':
    'sup_douyin',
    'Hm_lpvt_5d77c979053345c4bd8db63329f818ec':
    '1685604058',
    'csrf_session_id':
    '48f08f811499ab7c9154e69b51f0ffcb',
    'csrftoken':
    'FIerUNA15Wao2k7qjGtlz9ZbXwrrMHOu',
    'tt_webid':
    '7239614287542470181',
    'msToken':
    'Vv-kNARMQBfkR5AdTH2Bldc5CvBg1JBogg2Pklr_vSfTfln3w5VxM7Kfx2jDR__v4CWCGqVHiUlB_naaIaVeTMeWxEz41yI59r1Ue0yLVxU=',
}

headers = {
    'authority':
    'www.xingtu.cn',
    'accept':
    'application/json, text/plain, */*',
    'accept-language':
    'zh-CN,zh;q=0.9',
    'agw-js-conv':
    'str',
    'content-type':
    'application/json',
    # 'cookie': 'Hm_lvt_5d77c979053345c4bd8db63329f818ec=1685603902; ttcid=3e0d9411c3fd45a29c7a627c0b6f9ff947; tt_scid=keDLRKc9htpnkVz5WLRgHP3xLEKCL0oWWd5ZwPHbCb5cq.x7sOkxc6kg4z3OCZyi1376; star_login_type=sup_douyin; Hm_lpvt_5d77c979053345c4bd8db63329f818ec=1685604058; csrf_session_id=48f08f811499ab7c9154e69b51f0ffcb; csrftoken=FIerUNA15Wao2k7qjGtlz9ZbXwrrMHOu; tt_webid=7239614287542470181; msToken=Vv-kNARMQBfkR5AdTH2Bldc5CvBg1JBogg2Pklr_vSfTfln3w5VxM7Kfx2jDR__v4CWCGqVHiUlB_naaIaVeTMeWxEz41yI59r1Ue0yLVxU=',
    'origin':
    'https://www.xingtu.cn',
    'referer':
    'https://www.xingtu.cn/creative/visitor/market/index',
    'sec-ch-ua':
    '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-origin',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-csrftoken':
    'FIerUNA15Wao2k7qjGtlz9ZbXwrrMHOu',
    'x-login-source':
    '1',
    'x-secsdk-csrf-token':
    '000100000001f82c8cc8cde26aace4f757f115ca173e4645a4aee283b20f0b570bafebe7937517647989bb008550',
}

json_data = {
    'filters': {
        'first_category_id': '200',
        'project': 0,
    },
    'page': 1,
    'limit': 5,
}

response = requests.post('https://www.xingtu.cn/gw/api/search/spu',
                         cookies=cookies,
                         headers=headers,
                         json=json_data)
print(response.json())
