#-*-coding:utf-8-*-
import requests
import re
import string
import pymysql.cursors


def get1(pn):#获取分页连接
    url1="http://vod.cnzol.com/html/kehuan/index%d.html" %pn
    html = requests.get(url1)
    #html.encoding = 'gbk'
    h1=html.text
    #print(h1)
    reg = r'<dd><strong><a href="(.*?)">'#取出内页
    r1= re.findall(reg,h1)
    return r1
def get_start():
    url1="http://vod.cnzol.com/html/kehuan/1_user.html"
    html = requests.get(url1)
    #html.encoding = 'gbk'
    h1=html.text
    #print(h1)
    reg = r'<dd><strong><a href="(.*?)">'#取出内页
    r1= re.findall(reg,h1)
    return r1

    #print(r1)第一个分页链接的爬取


#     url2="http://www.ygdy8.net/html/gndy/oumei/index.html"
#     html = requests.get(url2)
#     html.encoding = 'gbk'
#     h1=html.text
#     print(h1)
#     reg = r'''
#     <b>
# 		<a class=ulink href='.*?'>[.*?]</a>
# 		<a href="(.*?)" class="ulink">.*?</a>
# 	</b>
# '''
#     R1 = re.findall(reg,h1)
#     print(R1)


    # reg = '''<xml><ToUserName><!\[CDATA\[(.*?)\]\]></ToUserName>
    # <FromUserName><!\[CDATA\[(.*?)\]\]></FromUserName>
    # <CreateTime>(.*?)</CreateTime>
    # <MsgType><!\[CDATA\[text\]\]></MsgType>
    # <Content><!\[CDATA\[(.*?)\]\]></Content>
    # <MsgId>.*?</MsgId>
    # </xml>'''
    # ToUserName, FromUserName, CreateTime, Content = re.findall(reg, i)[0]
    #print(html.text)
def get2(url):#分页爬取
    html1=requests.get(url)
    html1.encoding = 'utf-8'#网页编码定义
    h2=html1.text
    reg2=r'<h3>(.*?)</h3>'#取出标题
    title = re.findall(reg2, h2)[0]
    reg2=r'下载页面</div>(.*?)<strong><span style="color: #ff0000">'
    reg2=re.compile(reg2,re.S)#re.S可匹配多行#编译正则表达式
    content=re.findall(reg2,h2)[0]
    reg2=r'<a href="(.*?)"><font color="#106492" size="1">'
    downnurl = re.findall(reg2, h2)[:]
    return title,downnurl,content
if __name__=='__main__':
    connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='alex150750',
            db='django',
            charset='utf8', )#连接数据库
    # try:
    #     with connection.cursor() as cursor:
    #         sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`,`timestamp`) VALUES (%s, %s,%s,%s)"
    #         cursor.execute(sql, ('金刚狼', '好电影好电影', 'http://text.org', '2017-04-14 09:24:46.000000'))
    #     connection.commit()
    # finally:
    #     connection.close()
    #for id in range()
    for f in get_start():#第一次爬取
        title,downurl,content = get2(f)
        #print(downurl)
        print(len(downurl))
        if len(downurl)!=0:#下载链接数量判断并写入数据库
            if len(downurl)==1:
                string1=downurl[-1]
                print('共一条数据连接正在写入数据')
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`) VALUES (%s, %s,%s)"
                        cursor.execute(sql, (title, content, string1))
                    connection.commit()
                finally:
                    pass

            else:
                srting2=downurl[-2]
                string3=downurl[-1]
                string1=srting2+"\r\n"+string3
                print('选择两条数据连接正在写入数据')
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`) VALUES (%s, %s,%s)"
                        cursor.execute(sql, (title, content, string1))
                    connection.commit()
                finally:
                    print('保存成功......')


        else:
            string1='该电影因版权问题停止下载'
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`) VALUES (%s, %s,%s)"
                    cursor.execute(sql, (title, content, string1))
                connection.commit()
            finally:
                print('保存成功......')
    #connection.close()

        # url="".join(dwonurl)
        # print(url)
        # print(type(url))
        # break
        # with connection.cursor() as cursor:
        #     sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`,`timestamp`) VALUES (%s, %s,%s,%s)"
        #     cursor.execute(sql, (title, content, dwonurl, '2017-04-14 09:24:46.000000'))
    for n in range(2, 11):#2-10页的抓取
        print(n)
        for i in get1(n):
            title, dwonurl,content = get2(i)
            print(len(downurl))
            if len(downurl) != 0:  # 下载链接数量判断并写入数据库
                if len(downurl) == 1:
                    string1 = downurl[-1]
                    print('共一条数据连接正在写入数据')
                    try:
                        with connection.cursor() as cursor:
                            sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`) VALUES (%s, %s,%s)"
                            cursor.execute(sql, (title, content, string1))
                        connection.commit()
                    finally:
                        pass

                else:
                    srting2 = downurl[-2]
                    string3 = downurl[-1]
                    string1 = srting2 + "\r\n" + string3
                    print('选择两条数据连接正在写入数据')
                    try:
                        with connection.cursor() as cursor:
                            sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`) VALUES (%s, %s,%s)"
                            cursor.execute(sql, (title, content, string1))
                        connection.commit()
                    finally:
                        print('保存成功......')


            else:
                string1 = '该电影因版权问题停止下载'
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `text1_movie` (`title`, `body`,`downurl`) VALUES (%s, %s,%s)"
                        cursor.execute(sql, (title, content, string1))
                    connection.commit()
                finally:
                    print('保存成功......')
    connection.close()




            # Create a new record


        # connection is not autocommit by default. So you must commit to save
        # your changes.
        # connection.commit()



