# /usr/bin/env python
# coding=utf-8
 
import httplib
import hashlib
import urllib
import random


# appid = '20151113000005349'
# secretKey = 'osubCEzlGjzvw8qdQc41'
appid = '20160604000022732'
secretKey = 'O8bS3cjHGJJLDlOz_c2_'

httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
# m1 = md5.new()
m1 = hashlib.md5()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
furl="http://api.fanyi.baidu.com"+myurl
print furl
try:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    sResult = response.read()
    # 解析出中文译文
    import log4py
    dResult = dict(eval(sResult))['trans_result'][0]['dst']
    print type(dResult)
    uRes = unicode(dResult)
    print isinstance(dResult, unicode)
    print dResult.encode('utf-8')

    log4py.level['info'](dResult)
    # import codecs
    # output = codecs.open('data.txt', 'a', 'utf-8')
    # content = unicode(dict(eval(sResult))['trans_result'][0]['dst'], 'utf-8')
    # output.write(content)
    # output.close()

except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
