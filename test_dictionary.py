__author__ = 'sj'
# -*- coding:utf-8 -*-

import urllib,urllib2,json,re,random

def link():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    data = {}
    data['type'] = 'AUTO'
    data['i']= param
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    req = urllib2.Request(url,urllib.urlencode(data))
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')
    content = urllib2.urlopen(req)
    result = json.loads(content.read())['translateResult'][0][0]['tgt']
    print result

while True:

    try:
        url_1 = 'http://www.kuaidaili.com/proxylist/1/'
        data_1 = {}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
        req_1 = urllib2.Request(url_1,urllib.urlencode(data_1),headers)
        html = urllib2.urlopen(req_1).read()
        html_ip = re.compile(r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
        iplist = html_ip.findall(html)
        ip = random.choice(iplist)
        proxy = {'http':ip}
        proxy_support = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxy_support)
        #opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')]
        urllib2.install_opener(opener)
        param = raw_input('请输入内容：')
        if param == 'Q' or param == 'q':
            print '程序退出'
            break
        else:
            link()
    except Exception as e:
        print 'link error or link overtime'
        break