#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
from pandas import json_normalize


# In[2]:


def convert_json_to_csv(json_data, csv_file):
    df = pd.read_json(json_data)
    df.to_csv(csv_file, index=False)


# In[3]:


#curl for charging sessions

"""
curl 'https://account.chargeplacescotland.org/api/v2/poi/chargepoint/dynamic' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-GB-oxendict,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://chargeplacescotland.org' \
  -H 'Referer: https://chargeplacescotland.org/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  -H 'api-auth: c3VwcG9ydCtjcHNhcGlAc3dhcmNvLmNvbTpreWJUWCZGTyQhM3FQTnlhMVgj' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --compressed
  
"""


# In[8]:


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


# In[9]:


sessions = get_sessions()


# In[10]:


sessions


# In[ ]:





# In[ ]:




