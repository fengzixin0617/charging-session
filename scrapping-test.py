#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
from pandas import json_normalize
import datetime


def get_sessions():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-GB-oxendict,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://chargeplacescotland.org',
        'Referer': 'https://chargeplacescotland.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'api-auth': 'c3VwcG9ydCtjcHNhcGlAc3dhcmNvLmNvbTpreWJUWCZGTyQhM3FQTnlhMVgj',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    response = requests.get('https://account.chargeplacescotland.org/api/v2/poi/chargepoint/dynamic', headers=headers)
    return response.json()

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
sessions = get_sessions()
with open('sessions' + timestamp + '.json', 'w') as f:
    json.dump(sessions, f)



