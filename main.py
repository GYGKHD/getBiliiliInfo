import os
import random
import threading
import time
from datetime import datetime

import requests
import csv

import yaml

with open('config.yml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)


Cookie  = data.get('Cookie')
print(Cookie)
head = [
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
]



api_url = f'https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd'
video_api_url = 'https://api.bilibili.com/x/web-interface/view?bvid='

def getData(dataflie):
    while(1):
        headers = {
            'User-Agent': random.choice(head),
            'Cookie': Cookie
        }
        if os.path.exists("data/" + str(dataflie) + '.csv'):
            csvData = []
        else:
            csvData = [
                ['bvid', '标题', '分区', '发布时间', '作者id', '播放量',
                 '弹幕', '收藏', '评论', '分享', '点赞', '硬币']
            ]
        response = requests.get(api_url,headers=headers)


        if response.status_code == 200:

            data = response.json()
            for item in data['data']['item']:
                headers = {
                    'User-Agent': random.choice(head),
                }
                videoRes = requests.get(video_api_url + item['bvid'], headers=headers)
                videoData = videoRes.json()
                itemdata = [videoData['data']['bvid'],
                            videoData['data']['title'],
                            videoData['data']['tname'],
                            videoData['data']['ctime'],
                            videoData['data']['owner']['mid'],
                            videoData['data']['stat']['view'],
                            videoData['data']['stat']['danmaku'],
                            videoData['data']['stat']['favorite'],
                            videoData['data']['stat']['reply'],
                            videoData['data']['stat']['share'],
                            videoData['data']['stat']['like'],
                            videoData['data']['stat']['coin']]
                csvData.append(itemdata)
                # print(item['bvid'], item['title'])

            with open("data/" + str(dataflie) + '.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(csvData)
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_time + "已爬取30条")

threads = []
for i in range(1):
    thread = threading.Thread(target=getData,args=(i,))
    thread.start()
    threads.append(thread)

# 等待所有线程结束
for thread in threads:
    thread.join()