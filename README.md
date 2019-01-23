# hc-requests-redis

proxy_test.py 是代理测试　单个测试没有问题

hc.py　是主文件

config.py　是配置文件　　这里分离得比较少，可以把更多的东西写到里面去　　看个人习惯

item.json  是一些抓取的数据格式



selenium 是获取所有的link入队列　　整个到过程分为两部分，这是第一部分
当然也可以直接存redis也没问题

写的selenium一样很粗糙，没有显示等待，需要的可以自行完善


第二部分就是从redis取出url进行get解析啦，这里我脑子短路，先把url和tag先给到mongo再存入redis，简直就是多此一举，不说了，这里我附了一个从mongodb转到redis的小脚本，简单之极

把hc.py　拷贝几份放到几台不同的服务器上跑跑，我用的是两台ubuntu　和一台debian,数据存在ubuntu上，修改相应的mongodb和redis配置即可

对于get url　有很多中方法，甚至不用python也可以很容易做到，我经常用的事requests和urllib　代理的话可谓一波三折，之前在别的代码测试是完全没有问题的，这里却不能代理，无奈用了socks　　又出现了socket 104错误，这个需要点网络编程的知识，悲伤之极，不说了，代码总体可以跑，但是并没有能够做到完全自动化爬取，需要完善更多，这是一个尝试新思路的项目，体会一下即可．



