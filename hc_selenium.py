import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from lxml import etree
import pymongo

class Selenium():
    def __init__(self, timeout=None):
        self.logger = logging.getLogger(__name__)
        self.timeout = 20
        self.browser = webdriver.Chrome()
        # self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['new_hc']

    def __del__(self):
        self.browser.close()

    def process(self,url,tag):
        self.logger.debug('Chrome is Starting')
        try:
            self.browser.get(url)
            time.sleep(0.5)
            # ActionChains(self.browser).send_keys(Keys.DOWN).perform()
            try:
                js = "var q=document.documentElement.scrollTop=500"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=1200"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=1800"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=2500"
                self.browser.execute_script(js)
                time.sleep(1)
                js = "var q=document.documentElement.scrollTop=3200"
                self.browser.execute_script(js)
                time.sleep(1)
                js = "var q=document.documentElement.scrollTop=3700"
                self.browser.execute_script(js)
                time.sleep(1)
            except:
                js = "var q=document.documentElement.scrollTop=500"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=1000"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=1500"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=2300"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=3500"
                self.browser.execute_script(js)
                time.sleep(0.5)
                js = "var q=document.documentElement.scrollTop=4000"
                self.browser.execute_script(js)
            self.parse_detail(self.browser.page_source,tag)
        except TimeoutException:
            ActionChains(self.browser).send_keys(Keys.F5).perform()
            time.sleep(1)
            return self.process(url,tag)
        return self.browser

    def parse_detail(self, response,tag):
        # print(response.url)
        # item = response.meta['item']
        doc = etree.HTML(response)
        urls = doc.xpath("//div[@class='picmid pRel']")
        print(len(urls))
        for url in urls:
            sub_url = url.xpath("./a/@href")[0]
            # print(sub_url)
            if 'http' in sub_url:
                continue
            sub_url = 'https:' + sub_url
            item = {'link':sub_url,'tag': tag}
            if self.db['link'].update({'link':sub_url},{'$set': item},True):
                print('成功保存到mongo',tag,sub_url)
            else:
                print('No Mongo')
            # # yield item
            # yield scrapy.Request(sub_url,  callback=self.parse_sh, dont_filter=True)
        page = doc.xpath("//span[@class='page_next page-n']/a[@title='下一页']/@href")
        if page:
            next_page = 'https:' + page[0]
            print('当前页', next_page, '-------------')
            return self.process(next_page,tag)
            # yield scrapy.Request(next_page,callback=self.parse_detail,dont_filter=True)
        else:
            print("页面枯竭")
            pass

    def run(self):
        # print(self.db.get_collection('hc').find({}).count())
        for url in self.db.get_collection('link').find({}):
            print(url)
            self.process(url['big_link'],url['tag'])
            # self.parse_detail(html)

if __name__ == '__main__':
    hc = Selenium()
    hc.run()



# import requests
# import pymongo
# from lxml import etree
# client = pymongo.MongoClient('localhost')
# db = client['new_hc']
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
# response = requests.get("http://www.js.hc360.com/",headers=headers)

