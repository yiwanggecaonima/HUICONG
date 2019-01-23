# -*- coding:utf-8 -*-
import json
import re
import redis
import pymongo
import requests
pool = redis.ConnectionPool(host='127.0.0.1', port=6379,db=0)
r = redis.Redis(connection_pool=pool)

# r = redis.Redis.from_url("redis://127.0.0.1:6379/3", decode_responses=True) 几种连接redis数据库的格式
# r = redis.Redis(host='',port=6379,db=11,password='')


#　这是从redis拿出数据　注意如果是单引要变双引　　否则报错，然后转换成json格式，因为进去的是byte
import json
import re
for i in range(1,5):
   　da = r.get(i)
    string = str(da,'utf-8')
    string = re.sub("\'",'\"',string)
    s = json.loads(string)
    print(type(s))
    response = requests.get(s['link']).text
    print(response)


# 这是从mongo取出数据入redis　用的是set
client = pymongo.MongoClient('',27017)
db = client['scrapy_hc']
for data in db['link'].find({},{'_id':0}):
     if r.sadd('j_urls',data):
         print("++++++++++++++")
