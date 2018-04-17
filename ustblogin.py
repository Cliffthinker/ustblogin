import urllib.request
import urllib.parse
from lxml import etree
import http.cookiejar

def login(username='41521238',password='08228739'):  
    url = 'http://202.204.48.66/'

    #创建一个cookie对象来保存cookie
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie) #创建一个cookie的处理器
    opener = urllib.request.build_opener(handler)#构建一个handler对象,定制opener


    data =  {'DDDDD':username,
        'upass':password,
        'v6ip':'2001%3A0da8%3A0208%3Ac240%3A5d90%3A03aa%3A49c7%3Ae136',
        '0MKKey':'123456789'}
        


    data1=urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data1)
    #req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')
    req.add_header('User-Agent','Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.116Safari/537.36Edge/15.15063')

    response = opener.open(req)
       
    html = response.read().decode('gb2312')
    #print(html)
    html = etree.HTML(html)
    
    test = html.xpath('//div[@class="d"]/form[@style="width:100%;"]/p/span/text()')
    '''test2 = html.xpath('//div[@class="m"]/div[@class="m_r"]/div[@class="d"]/form[@style="width:100%;"]/p/span/text()')   
    print(test2)'''
    flag = 0
    if test == []:
        print ('failed! check your accout and password.')
    else:
       print(test[0])
       flag = 1
        
    input('\nfinished')
 
if __name__ == '__main__':
    login()  
    
    