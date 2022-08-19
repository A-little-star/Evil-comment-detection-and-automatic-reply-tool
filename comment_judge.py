import pandas as pd
import numpy as np
import json
import requests
data = pd.read_csv("V_BV1fU4y1e7HJ.csv")
data = np.array(data)
comment = {}
for i in range(21):
    comment[i] = data[i][5]

token = requests.request('POST',
                    'https://wenxin.baidu.com/younger/portal/api/oauth/token',
                data={
                    'grant_type':'client_credentials',
                    'client_id':'CGZk7AcLBvsuWHz8XIe2Zttk12pjWP9w',
                    'client_secret':'4e0PNWsSquGTnQQEqkRcGmlOQVzRHvVa'},
                    timeout=3)
token = json.loads(token.text)['data']
url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernie/3.0/zeus"
for i in range(21):
    payload={
    'text': comment[i]+',这是恶评吗？ ',
    'seq_len': 8,
    'task_prompt': 'SentimentClassification',
    'dataset_prompt': '',
    'access_token': token,
    'topk': 1,
    'stop_token': ''
    }
    response = requests.request("POST", url, data=payload)
    print(response.text)

#response = requests.request("POST", url, data=payload)


