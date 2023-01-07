# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 10:10
# @Author  : AI悦创
# @FileName: DelayWait.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from urllib import parse  # 解析 URL
from datetime import datetime  # 获取时间（标注时间）时间加减
import time, requests  # time 实现睡眠 requests 爬虫库


class DelayWait(object):
    """
    1. 在一个时间段中请求的次数过多被封禁；
    2. 同一个 IP 访问同一个主站的请求间隔过短或者说太过于相同从而被封禁；
    所谓，赚钱的方法都写在宪法里面了，那解决的方法都写着问题里面了。 解决方法也很简单：
    a. 避免对使用同一个 IP 请求也就是换 IP 但是我们本文不是讲这个的；
    b. 避免对过快的请求同一个主站；
    c. 让每个 get 请求的间隔有所不同；time.sleep()
    """

    def __init__(self, delay=3):
        self.delay = delay
        self.urls = dict()  # 存储各种 URL,域名:time

    def wait(self, url):
        netloc = parse.urlparse(url).netloc
        # 解析我们的 URL，来对比每次访问的主站，是否是同一个主站，同一个就是使用该延迟插件，不是就不用啦！
        # 因为，我们封 IP 其实就是，快速重复访问同一个网站,才有可能被封；
        lastOne = self.urls.get(netloc)  # get 没有提取到数据的时候，会返回 None
        if lastOne and self.delay > 0:
            timeWait = self.delay - (datetime.now() - lastOne).seconds
            if timeWait > 0:
                time.sleep(timeWait)
        self.urls[netloc] = datetime.now()


if __name__ == '__main__':
    urls = ["https://bornforthis.cn"] * 10
    d = DelayWait()
    for url in urls:
        html = requests.get(url)
        d.wait(url)
        print(html.status_code)