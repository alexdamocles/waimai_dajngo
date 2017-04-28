import requests
import re


def get_photo_jpg(page):
    #url1='http://news.meishujia.cn/?act=app&appid=4115&mid=3311&p=view'#原创新闻
    url1='http://news.meishujia.cn/?act=app&appid=4115&mid=%d&p=view'%page
    html1=requests.get(url1)
    html1.encoding = 'gbk'      #网页编码定义
    h2=html1.text
    reg2=r'src="(.*?).jpg"'       #取出标题
    photourl = re.findall(reg2, h2)
    # error = 'http://m1.thumb.cdn.zgzsys.com/cache/img/4075/15-02-05/1423127433_afile'
    # if photourl[0] != error:        #如果get到的图片列表中的1和网页base。html里的模板图片不一样
    #     if photourl[1] != error:    #如果get到的图片列表中的2和网页base。html里的模板图片不一样
    #
    #         return photourl
    #     else:
    #         print('get到图片不正确正在转换get模式..')
    #         secondurl = get_photo_png(page)  #搜索png图片
    #         if secondurl[1] != error:
    #             map(photo_png,photourl)
    #             return photourl
    #         else:                           #这就彻底没辙了
    #             print('没有图片吧。。')
    #             return 0
    # else:
    #     print('get到不正确图片正在转换get模式..')
    #
    #     secondurl=get_photo_png(page)       #搜索png图片
    #     if secondurl[0] !=error:
    #         map(photo_png, photourl)
    #         return photourl
    #     else:                               # 这就彻底没辙了
    #         print('没有图片吧。。')
    #         return 0
    # for i in
    # return photourl1

def get_photo_png(page):
    #url1='http://news.meishujia.cn/?act=app&appid=4115&mid=3311&p=view'#原创新闻
    url1='http://news.meishujia.cn/?act=app&appid=4115&mid=%d&p=view'%page
    html1=requests.get(url1)
    html1.encoding = 'gbk'      #网页编码定义
    h2=html1.text
    reg2=r'src="(.*?).png"'       #取出标题
    second = re.findall(reg2, h2)
    return second
def photo_jpg(photourl):
    return photourl+'.jpg'

    pass

def photo_png(photourl):
    return photourl + '.png'
    pass

if __name__=='__main__':
    for i in range(3305,3309):
        print('编号%d文章链接' % i)
        url1=get_photo_jpg(i)
        print(url1)

        #print()



