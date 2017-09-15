#!/usr/bin/python
import urllib
import urllib2
import zlib
import time
import json

http_headers = {
        'Host': 'api.yqqjp.com',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Referer': 'http://m.yqqjp.com/weixin/product-detail.html?cid=593',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'web_yqqjpFromApp=default; cc_id=0; c_id=1039'
        }
def load_cinfo(cid):
    print '>>>  start load ' + cid + ' detail info'
    url = "http://api.yqqjp.com/index.php?c=cate&a=info&cid="+cid+"&sertype=yqqjp&_="+str(int(round(time.time(),3)*1000))+"&cb=jsonp1"
    req = urllib2.Request(url,headers = http_headers)
    response = urllib2.urlopen(req)
    content = response.read()
    html = zlib.decompress(content,16+zlib.MAX_WBITS)
    jsonString = html.decode('utf-8')[7:-2]
    jsonData = json.loads(jsonString)
    infoString = json.dumps(jsonData["info"])
    fo = open('./output/'+cid+"_detail.json","wb")
    fo.write(infoString)
    fo.close()
    print 'end load '+ cid+" detail info <<<"

def load_jsonData(fname):
    with open(fname) as json_file:
        data = json.load(json_file)
        return  data

def main():
    cids = load_jsonData('cids.json')
    for cid in cids:
        load_cinfo(cid["cid"])

if __name__ == "__main__":
    main()
    print '---------load all data sucess ^V^-----------'
