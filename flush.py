import urllib2
import re
import random
from multiprocessing.dummy import Pool as ThreadPool 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
proxyPool = []
def get_proxy(proxyUrl):
    try:
        request = urllib2.Request(proxyUrl,None,headers)
        response = urllib2.urlopen(request)
    except urllib.error.URLError as e:
        print 'load proxy failed',e.reason
        return 
    else:
        html = response.read().decode('utf-8')
        pattern = re.compile(r'''<tr\sclass[^>]*>\s+
                <td\sclass[^>]*>.+</td>\s+
                <td>(.*)?</td>\s+
                <td>(.*)?</td>\s+
                <td>(.*)?</td>\s+
                <td\sclass[^>]*>(.*)?</td>\s+
                <td>(.*)?</td>\s+
                <td>(.*)?</td>\s+
                <td>(.*)?</td>\s+
                </tr>''',re.VERBOSE)
        proxys = pattern.findall(html)
        for proxy in proxys:
            if proxy[4] == 'HTTP':
                proxyPool.append(proxy[4]+'://'+proxy[0]+':'+proxy[1])
        print proxyPool

def changProxy():
    proxy = random.choice(proxyPool)
    proxyHandler = urllib2.ProxyHandler({"http":proxy})
    opener = urllib2.build_opener(proxyHandler)
    urllib2.install_opener(opener)
def refreshBlog(url):
    changProxy()
    blog_eader = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
            'Host':'blog.csdn.net',
            'Referer':'http://blog.csdn.net/',
            'GET':url
            }
    request = urllib2.Request(url,headers = blog_eader)
    try:
        response = urllib2.urlopen(request)
    except:
        pass
   # except urllib2.URLError as e:
   #     print 'refreshBlog failed',e.reason
   #     return 

bloglist = []
def refresh():
    for i in range(0,10000):
        bloglist.append("http://blog.csdn.net/sujun10/article/details/76427703")
    pool = ThreadPool(30)
    results = pool.map(refreshBlog, bloglist)
    pool.close()
    pool.join()

get_proxy("http://www.xicidaili.com/")
refresh()
