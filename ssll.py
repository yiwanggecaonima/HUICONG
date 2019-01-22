import re
# import urllib.request
# from urllib.error import URLError
# try:
#     proxy = urllib.request.ProxyHandler({"http":"http://223.8.147.185:4236"})
#     opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen("https://b2b.hc360.com/supplyself/510489481.html").read().decode("gbk")
#     print(data)
# except URLError:

import requests
try:
    response = requests.get('http://webapi.http.zhimacangku.com/getip?num=20&type=1&pro=&city=0&yys=0&port=1&pack=38903&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=',verify=False)
    a = response.text.split("\r\n")
    print(a)

except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

import pymongo
# client = pymongo.MongoClient("47.107.137.63", 27017,connect=True)
# for u in client['scrapy_hc']['hc_item_净水'].find():
#     print(u)


# import requests
# res = requests.get("http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=140000&city=140500&yys=0&port=1&pack=38903&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions=")
# print(res.text)
# ip_port = res.text.split(':')
# print(ip_port[0])
# print(ip_port[1])
f =['106.46.136.117:4237', '125.123.47.134:4225', '124.152.85.29:3012', '123.153.93.81:4214', '182.100.242.223:4256', '122.242.80.26:4224', '182.87.240.53:4250', '49.88.169.18:2444', '123.152.43.22:2682', '101.70.8.190:4214', '36.33.31.118:6436', '125.123.47.70:4225', '120.34.216.156:4216', '49.79.36.7:4206', '60.13.50.238:3012', '175.174.94.19:4216', '111.79.173.81:5632', '115.219.73.119:4217', '182.111.92.123:4276', '116.54.239.143:4284', '58.218.26.128:4224', '115.213.226.173:2852', '182.34.17.243:9077', '115.221.9.216:2316', '59.60.141.87:4271', '220.189.86.237:2549', '36.34.15.88:6436', '115.217.21.41:4270', '49.88.169.189:5521', '59.62.252.62:4256', '']
s =['183.163.37.253:4251', '117.94.153.131:4734', '42.87.77.79:4211', '222.185.22.88:4216', '125.106.132.175:7305', '112.194.71.69:4216', '182.37.93.71:6856', '112.194.68.100:4226', '115.208.162.131:4223', '60.166.86.227:4208', '60.186.45.7:1246', '1.25.147.192:6410', '112.84.72.200:4278', '125.64.127.172:4286', '115.226.240.9:4208', '117.67.131.26:2644', '106.46.136.112:4237', '114.224.84.77:4263', '125.123.44.139:4225', '117.67.245.78:4208', '180.118.128.42:3217', '106.110.145.170:4258', '112.122.218.24:4224', '27.28.249.193:4216', '182.45.63.230:6856', '182.99.134.189:4201', '182.87.241.51:4250', '223.215.97.232:4286', '125.89.43.100:4223', '113.120.36.207:4242', '']