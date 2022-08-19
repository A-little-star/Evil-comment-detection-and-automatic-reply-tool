import pandas as pd
import numpy as np
import json
import requests
data = pd.read_csv("V_BV1BW4y127s3.csv")
data = np.array(data)
comment = {}
for i in range(21):
    comment[i] = data[i][5]
    print(comment[i])
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
    payload = {
        'text': '小李：'+comment[i]+'。小张：',
        'seq_len': 128,
        'task_prompt': '',
        'dataset_prompt': '',
        'access_token': token,
        'topk': 10,
        'stop_token': '',
        'is_unidirectional': 1
    }
    response = requests.request("POST", url, data=payload)
    print(response.text)
