#-*-coding:utf-8-*-
import requests
import re
import time
# def get1(pn):#now52872
#     url1="http://news.meishujia.cn/?act=app&appid=4096&mid=%d&p=view" %pn
#     html = requests.get(url1)
#     html.encoding = 'gbk'
#     h1=html.text
#     #print(h1)
#     reg = r'<li class="nw_liebi"><span>(.*?)</span><em>■</em><A HREF="(.*?)" target=_blank>(.*?)</A></li>'#取出内页
#     time,url,title= re.findall(reg,h1)
#     return time,url,title

# def get_start():
#     url1="http://news.meishujia.cn/index.php?page=1&act=app&appid=4096&fenlei=57"
#     html = requests.get(url1)
#
#     #html.encoding = 'gbk'
#     h1=html.text
#     reg = r'<li class="nw_liebi"><span>.*?</span><em>■</em><A HREF="(.*?)" target=_blank>.*?</A></li>'  # 取出内页
#     url = re.findall(reg, h1)
#     return  url
    #print(h1)
    #reg = r'<dd><strong><a href="(.*?)">'#取出内页
    #rstart= re.findall(reg,h1)



#s=requests.session()

payload = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': ' / wEPDwUKMjA0MTUxNzI2OQ9kFgICAQ9kFgQCAQ8PFgIeB1Zpc2libGVoZGQCAg8PFgIfAGdkFgQCCA8WAh8AaGQCCg8WAh8AaBYCAgQPD2QWBB4Hb25jbGljawU3dGhpcy5zcmM9Jy4uL1BsdXMvVmFsaWRhdGVDb2RlLmFzcHg / bj0nKyBNYXRoLnJhbmRvbSgpOx4Lb25tb3VzZW92ZXIFGHRoaXMuc3R5bGUuY3Vyc29yPSdoYW5kJ2Rk9DkYht + mJC9S1QWFSb7blw + VyAU =',
    '__VIEWSTATEGENERATOR': '82312306',
    'UserName': 'sxfu_ysgc',
    'UserPass': 'ysgcxy',
    'ImageButton1': '登录'
}

pp = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/ wEPDwUJLTQyNzA4NjE1D2QWAmYPZBYCZg9kFgICAQ9kFhJmDw8WAh4KdG9wbmF2dGV4dAUM5re75Yqg5paH56ugZGQCAQ8PFgYeCEZpZWxkWE1MBdxlPD94bWwgdmVyc2lvbj0iMS4wIj8 + DQo8TW9kZWw + DQogIDxGaWVsZCBOYW1lPSJUaXRsZSIgT3JkZXJJRD0iMCIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjAiPg0KICAgIDxEaXNhYmxlZD50cnVlPC9EaXNhYmxlZD4NCiAgICA8RmllbGRBbGlhcz7moIfpopg8L0ZpZWxkQWxpYXM + DQogICAgPFRpcHM + DQogICAgPC9UaXBzPg0KICAgIDxGaWVsZFR5cGU + MDwvRmllbGRUeXBlPg0KICAgIDxGaWVsZExldmVsPjA8L0ZpZWxkTGV2ZWw + DQogICAgPEZpZWxkV2lkdGg + MzAwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4NCiAgICA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQ + DQogICAgPC9BbGxvd0ZpbGVFeHQ + DQogICAgPE1heEZpbGVTaXplPg0KICAgIDwvTWF4RmlsZVNpemU + DQogICAgPERlZmF1bHRWYWx1ZT4NCiAgICA8L0RlZmF1bHRWYWx1ZT4NCiAgICA8T3B0aW9ucz5CYXNpYzwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjE8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iQXR0cmlidXRlIiBPcmRlcklEPSIyIiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI1MyIgTWFuYWdlSXRlbT0iMSI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPueJueauiuWxnuaApzwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4yMDA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPjAwMDAwMDE8L0RlZmF1bHRWYWx1ZT4NCiAgICA8T3B0aW9ucz4NCiAgICA8L09wdGlvbnM + DQogICAgPFRvb2xCYXI + QmFzaWM8L1Rvb2xCYXI + DQogICAgPElucHV0SXRlbT4xPC9JbnB1dEl0ZW0 + DQogICAgPENvbnRyaWJ1dGlvbkl0ZW0 + MDwvQ29udHJpYnV0aW9uSXRlbT4NCiAgICA8U2VhcmNoSXRlbT4wPC9TZWFyY2hJdGVtPg0KICAgIDxDb2xsZWN0SXRlbT4wPC9Db2xsZWN0SXRlbT4NCiAgICA8TXVzdEZpbGxJdGVtPjA8L011c3RGaWxsSXRlbT4NCiAgPC9GaWVsZD4NCiAgPEZpZWxkIE5hbWU9IkNsYXNzSUQiIE9yZGVySUQ9IjEiIFBhcmVudEZpZWxkSUQ9IjAiIEdyb3VwSUQ9IjUzIiBNYW5hZ2VJdGVtPSIxIj4NCiAgICA8RGlzYWJsZWQ + dHJ1ZTwvRGlzYWJsZWQ + DQogICAgPEZpZWxkQWxpYXM + 5omA5bGe5qCP55uuPC9GaWVsZEFsaWFzPg0KICAgIDxUaXBzPg0KICAgIDwvVGlwcz4NCiAgICA8RmllbGRUeXBlPjA8L0ZpZWxkVHlwZT4NCiAgICA8RmllbGRMZXZlbD4wPC9GaWVsZExldmVsPg0KICAgIDxGaWVsZFdpZHRoPjIwMDwvRmllbGRXaWR0aD4NCiAgICA8RmllbGRIZWlnaHQ + MTAwPC9GaWVsZEhlaWdodD4NCiAgICA8QWxsb3dGaWxlRXh0Pg0KICAgIDwvQWxsb3dGaWxlRXh0Pg0KICAgIDxNYXhGaWxlU2l6ZT4NCiAgICA8L01heEZpbGVTaXplPg0KICAgIDxEZWZhdWx0VmFsdWU + DQogICAgPC9EZWZhdWx0VmFsdWU + DQogICAgPE9wdGlvbnM + DQogICAgPC9PcHRpb25zPg0KICAgIDxUb29sQmFyPkJhc2ljPC9Ub29sQmFyPg0KICAgIDxJbnB1dEl0ZW0 + MTwvSW5wdXRJdGVtPg0KICAgIDxDb250cmlidXRpb25JdGVtPjE8L0NvbnRyaWJ1dGlvbkl0ZW0 + DQogICAgPFNlYXJjaEl0ZW0 + MDwvU2VhcmNoSXRlbT4NCiAgICA8Q29sbGVjdEl0ZW0 + MDwvQ29sbGVjdEl0ZW0 + DQogICAgPE11c3RGaWxsSXRlbT4xPC9NdXN0RmlsbEl0ZW0 + DQogIDwvRmllbGQ + DQogIDxGaWVsZCBOYW1lPSJUdXJuVXJsIiBPcmRlcklEPSIzIiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI1MyIgTWFuYWdlSXRlbT0iMCI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPui9rOWQkemTvuaOpTwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4zNTA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjE8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iS2V5VGFncyIgT3JkZXJJRD0iNCIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjEiPg0KICAgIDxEaXNhYmxlZD5mYWxzZTwvRGlzYWJsZWQ + DQogICAgPEZpZWxkQWxpYXM + 5YWz6ZSu5a2XVEFHUzwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4yMDA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjA8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iQ29weUZyb20iIE9yZGVySUQ9IjUiIFBhcmVudEZpZWxkSUQ9IjAiIEdyb3VwSUQ9IjUzIiBNYW5hZ2VJdGVtPSIxIj4NCiAgICA8RGlzYWJsZWQ + ZmFsc2U8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPuadpea6kDwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4yMDA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjE8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iQXV0aG9yIiBPcmRlcklEPSI2IiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI1MyIgTWFuYWdlSXRlbT0iMSI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPuS9nOiAhTwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4yMDA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjA8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iQWRkRGF0ZSIgT3JkZXJJRD0iNyIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjEiPg0KICAgIDxEaXNhYmxlZD50cnVlPC9EaXNhYmxlZD4NCiAgICA8RmllbGRBbGlhcz7mm7TmlrDml7bpl7Q8L0ZpZWxkQWxpYXM + DQogICAgPFRpcHM + DQogICAgPC9UaXBzPg0KICAgIDxGaWVsZFR5cGU + MDwvRmllbGRUeXBlPg0KICAgIDxGaWVsZExldmVsPjA8L0ZpZWxkTGV2ZWw + DQogICAgPEZpZWxkV2lkdGg + MjAwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4xMDA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQ + DQogICAgPC9BbGxvd0ZpbGVFeHQ + DQogICAgPE1heEZpbGVTaXplPg0KICAgIDwvTWF4RmlsZVNpemU + DQogICAgPERlZmF1bHRWYWx1ZT4NCiAgICA8L0RlZmF1bHRWYWx1ZT4NCiAgICA8T3B0aW9ucz4NCiAgICA8L09wdGlvbnM + DQogICAgPFRvb2xCYXI + QmFzaWM8L1Rvb2xCYXI + DQogICAgPElucHV0SXRlbT4xPC9JbnB1dEl0ZW0 + DQogICAgPENvbnRyaWJ1dGlvbkl0ZW0 + MTwvQ29udHJpYnV0aW9uSXRlbT4NCiAgICA8U2VhcmNoSXRlbT4wPC9TZWFyY2hJdGVtPg0KICAgIDxDb2xsZWN0SXRlbT4xPC9Db2xsZWN0SXRlbT4NCiAgICA8TXVzdEZpbGxJdGVtPjE8L011c3RGaWxsSXRlbT4NCiAgPC9GaWVsZD4NCiAgPEZpZWxkIE5hbWU9IkludHJvIiBPcmRlcklEPSI4IiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI1MyIgTWFuYWdlSXRlbT0iMCI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPueugOimgeS7i + e7jTwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4yMDA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjE8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iQ29udGVudCIgT3JkZXJJRD0iOSIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjAiPg0KICAgIDxEaXNhYmxlZD50cnVlPC9EaXNhYmxlZD4NCiAgICA8RmllbGRBbGlhcz7lhbfkvZPlhoXlrrk8L0ZpZWxkQWxpYXM + DQogICAgPFRpcHM + DQogICAgPC9UaXBzPg0KICAgIDxGaWVsZFR5cGU + MDwvRmllbGRUeXBlPg0KICAgIDxGaWVsZExldmVsPjA8L0ZpZWxkTGV2ZWw + DQogICAgPEZpZWxkV2lkdGg + MjAwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4xMDA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQ + DQogICAgPC9BbGxvd0ZpbGVFeHQ + DQogICAgPE1heEZpbGVTaXplPg0KICAgIDwvTWF4RmlsZVNpemU + DQogICAgPERlZmF1bHRWYWx1ZT4NCiAgICA8L0RlZmF1bHRWYWx1ZT4NCiAgICA8T3B0aW9ucz4NCiAgICA8L09wdGlvbnM + DQogICAgPFRvb2xCYXI + QmFzaWM8L1Rvb2xCYXI + DQogICAgPElucHV0SXRlbT4xPC9JbnB1dEl0ZW0 + DQogICAgPENvbnRyaWJ1dGlvbkl0ZW0 + MTwvQ29udHJpYnV0aW9uSXRlbT4NCiAgICA8U2VhcmNoSXRlbT4wPC9TZWFyY2hJdGVtPg0KICAgIDxDb2xsZWN0SXRlbT4xPC9Db2xsZWN0SXRlbT4NCiAgICA8TXVzdEZpbGxJdGVtPjE8L011c3RGaWxsSXRlbT4NCiAgPC9GaWVsZD4NCiAgPEZpZWxkIE5hbWU9IkRlZmF1bHRQaWMiIE9yZGVySUQ9IjEwIiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI1MyIgTWFuYWdlSXRlbT0iMCI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPue8qeeVpeWbvjwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4zNTA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjE8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0i6aaW6aG157yp55Wl5Zu + MTM4MHg0NjAiIE9yZGVySUQ9IjE4IiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI1MyIgTWFuYWdlSXRlbT0iMSI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPummlumhtee8qeeVpeWbvjEzODB4NDYwLemdnuS4u + ermeeuoeeQhuaXoOmcgOS4iuS8oDwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4xMDwvRmllbGRUeXBlPg0KICAgIDxGaWVsZExldmVsPjE8L0ZpZWxkTGV2ZWw + DQogICAgPEZpZWxkV2lkdGg + MzUwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4xMDA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQ + anBnfHBuZ3xnaWY8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + MTAyNDA8L01heEZpbGVTaXplPg0KICAgIDxEZWZhdWx0VmFsdWU + DQogICAgPC9EZWZhdWx0VmFsdWU + DQogICAgPE9wdGlvbnM + DQogICAgPC9PcHRpb25zPg0KICAgIDxUb29sQmFyPkJhc2ljPC9Ub29sQmFyPg0KICAgIDxJbnB1dEl0ZW0 + MTwvSW5wdXRJdGVtPg0KICAgIDxDb250cmlidXRpb25JdGVtPjE8L0NvbnRyaWJ1dGlvbkl0ZW0 + DQogICAgPFNlYXJjaEl0ZW0 + MDwvU2VhcmNoSXRlbT4NCiAgICA8Q29sbGVjdEl0ZW0 + MDwvQ29sbGVjdEl0ZW0 + DQogICAgPE11c3RGaWxsSXRlbT4wPC9NdXN0RmlsbEl0ZW0 + DQogIDwvRmllbGQ + DQogIDxGaWVsZCBOYW1lPSJQcmlvcml0eSIgT3JkZXJJRD0iMTEiIFBhcmVudEZpZWxkSUQ9IjAiIEdyb3VwSUQ9IjUzIiBNYW5hZ2VJdGVtPSIwIj4NCiAgICA8RGlzYWJsZWQ + ZmFsc2U8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPuS8mOWFiOe6pzwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4wPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MDwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD41MDwvRmllbGRXaWR0aD4NCiAgICA8RmllbGRIZWlnaHQ + MTAwPC9GaWVsZEhlaWdodD4NCiAgICA8QWxsb3dGaWxlRXh0Pg0KICAgIDwvQWxsb3dGaWxlRXh0Pg0KICAgIDxNYXhGaWxlU2l6ZT4NCiAgICA8L01heEZpbGVTaXplPg0KICAgIDxEZWZhdWx0VmFsdWU + DQogICAgPC9EZWZhdWx0VmFsdWU + DQogICAgPE9wdGlvbnM + DQogICAgPC9PcHRpb25zPg0KICAgIDxUb29sQmFyPkJhc2ljPC9Ub29sQmFyPg0KICAgIDxJbnB1dEl0ZW0 + MTwvSW5wdXRJdGVtPg0KICAgIDxDb250cmlidXRpb25JdGVtPjE8L0NvbnRyaWJ1dGlvbkl0ZW0 + DQogICAgPFNlYXJjaEl0ZW0 + MDwvU2VhcmNoSXRlbT4NCiAgICA8Q29sbGVjdEl0ZW0 + MDwvQ29sbGVjdEl0ZW0 + DQogICAgPE11c3RGaWxsSXRlbT4wPC9NdXN0RmlsbEl0ZW0 + DQogIDwvRmllbGQ + DQogIDxGaWVsZCBOYW1lPSJIaXRzIiBPcmRlcklEPSIxMiIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjEiPg0KICAgIDxEaXNhYmxlZD50cnVlPC9EaXNhYmxlZD4NCiAgICA8RmllbGRBbGlhcz7ngrnlh7vmlbA8L0ZpZWxkQWxpYXM + DQogICAgPFRpcHMgLz4NCiAgICA8RmllbGRUeXBlPjA8L0ZpZWxkVHlwZT4NCiAgICA8RmllbGRMZXZlbD4wPC9GaWVsZExldmVsPg0KICAgIDxGaWVsZFdpZHRoPjUwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4xMDA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQgLz4NCiAgICA8TWF4RmlsZVNpemUgLz4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhciAvPg0KICAgIDxJbnB1dEl0ZW0 + MTwvSW5wdXRJdGVtPg0KICAgIDxDb250cmlidXRpb25JdGVtPjE8L0NvbnRyaWJ1dGlvbkl0ZW0 + DQogICAgPFNlYXJjaEl0ZW0 + MDwvU2VhcmNoSXRlbT4NCiAgICA8Q29sbGVjdEl0ZW0 + MTwvQ29sbGVjdEl0ZW0 + DQogICAgPE11c3RGaWxsSXRlbT4wPC9NdXN0RmlsbEl0ZW0 + DQogIDwvRmllbGQ + DQogIDxGaWVsZCBOYW1lPSJBcmVhIiBPcmRlcklEPSIxNCIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjEiPg0KICAgIDxEaXNhYmxlZD5mYWxzZTwvRGlzYWJsZWQ + DQogICAgPEZpZWxkQWxpYXM + 6YCJ5oup5Z + O5biCPC9GaWVsZEFsaWFzPg0KICAgIDxUaXBzPg0KICAgIDwvVGlwcz4NCiAgICA8RmllbGRUeXBlPjA8L0ZpZWxkVHlwZT4NCiAgICA8RmllbGRMZXZlbD4wPC9GaWVsZExldmVsPg0KICAgIDxGaWVsZFdpZHRoPjIwMDwvRmllbGRXaWR0aD4NCiAgICA8RmllbGRIZWlnaHQ + MTAwPC9GaWVsZEhlaWdodD4NCiAgICA8QWxsb3dGaWxlRXh0Pg0KICAgIDwvQWxsb3dGaWxlRXh0Pg0KICAgIDxNYXhGaWxlU2l6ZT4NCiAgICA8L01heEZpbGVTaXplPg0KICAgIDxEZWZhdWx0VmFsdWU + DQogICAgPC9EZWZhdWx0VmFsdWU + DQogICAgPE9wdGlvbnM + DQogICAgPC9PcHRpb25zPg0KICAgIDxUb29sQmFyPkJhc2ljPC9Ub29sQmFyPg0KICAgIDxJbnB1dEl0ZW0 + MTwvSW5wdXRJdGVtPg0KICAgIDxDb250cmlidXRpb25JdGVtPjE8L0NvbnRyaWJ1dGlvbkl0ZW0 + DQogICAgPFNlYXJjaEl0ZW0 + MDwvU2VhcmNoSXRlbT4NCiAgICA8Q29sbGVjdEl0ZW0 + MTwvQ29sbGVjdEl0ZW0 + DQogICAgPE11c3RGaWxsSXRlbT4wPC9NdXN0RmlsbEl0ZW0 + DQogIDwvRmllbGQ + DQogIDxGaWVsZCBOYW1lPSJJbnB1dGVyIiBPcmRlcklEPSIxMyIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNTMiIE1hbmFnZUl0ZW09IjEiPg0KICAgIDxEaXNhYmxlZD50cnVlPC9EaXNhYmxlZD4NCiAgICA8RmllbGRBbGlhcz7lvZXlhaXogIU8L0ZpZWxkQWxpYXM + DQogICAgPFRpcHM + DQogICAgPC9UaXBzPg0KICAgIDxGaWVsZFR5cGU + MDwvRmllbGRUeXBlPg0KICAgIDxGaWVsZExldmVsPjA8L0ZpZWxkTGV2ZWw + DQogICAgPEZpZWxkV2lkdGg + MjAwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4xMDA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQ + DQogICAgPC9BbGxvd0ZpbGVFeHQ + DQogICAgPE1heEZpbGVTaXplPg0KICAgIDwvTWF4RmlsZVNpemU + DQogICAgPERlZmF1bHRWYWx1ZT4NCiAgICA8L0RlZmF1bHRWYWx1ZT4NCiAgICA8T3B0aW9ucz4NCiAgICA8L09wdGlvbnM + DQogICAgPFRvb2xCYXI + QmFzaWM8L1Rvb2xCYXI + DQogICAgPElucHV0SXRlbT4xPC9JbnB1dEl0ZW0 + DQogICAgPENvbnRyaWJ1dGlvbkl0ZW0 + MTwvQ29udHJpYnV0aW9uSXRlbT4NCiAgICA8U2VhcmNoSXRlbT4wPC9TZWFyY2hJdGVtPg0KICAgIDxDb2xsZWN0SXRlbT4wPC9Db2xsZWN0SXRlbT4NCiAgICA8TXVzdEZpbGxJdGVtPjA8L011c3RGaWxsSXRlbT4NCiAgPC9GaWVsZD4NCiAgPEZpZWxkIE5hbWU9ImxlaWJpZSIgT3JkZXJJRD0iMTUiIFBhcmVudEZpZWxkSUQ9IjAiIEdyb3VwSUQ9IjYyIiBNYW5hZ2VJdGVtPSIwIj4NCiAgICA8RGlzYWJsZWQ + dHJ1ZTwvRGlzYWJsZWQ + DQogICAgPEZpZWxkQWxpYXM + 55Sf5rqQ57G75YirPC9GaWVsZEFsaWFzPg0KICAgIDxUaXBzPg0KICAgIDwvVGlwcz4NCiAgICA8RmllbGRUeXBlPjE8L0ZpZWxkVHlwZT4NCiAgICA8RmllbGRMZXZlbD4xPC9GaWVsZExldmVsPg0KICAgIDxGaWVsZFdpZHRoPjE2MDwvRmllbGRXaWR0aD4NCiAgICA8RmllbGRIZWlnaHQ + MTAwPC9GaWVsZEhlaWdodD4NCiAgICA8QWxsb3dGaWxlRXh0Pg0KICAgIDwvQWxsb3dGaWxlRXh0Pg0KICAgIDxNYXhGaWxlU2l6ZT4NCiAgICA8L01heEZpbGVTaXplPg0KICAgIDxEZWZhdWx0VmFsdWU + DQogICAgPC9EZWZhdWx0VmFsdWU + DQogICAgPE9wdGlvbnM + DQogICAgPC9PcHRpb25zPg0KICAgIDxUb29sQmFyPkJhc2ljPC9Ub29sQmFyPg0KICAgIDxJbnB1dEl0ZW0 + MTwvSW5wdXRJdGVtPg0KICAgIDxDb250cmlidXRpb25JdGVtPjE8L0NvbnRyaWJ1dGlvbkl0ZW0 + DQogICAgPFNlYXJjaEl0ZW0 + MDwvU2VhcmNoSXRlbT4NCiAgICA8Q29sbGVjdEl0ZW0 + MDwvQ29sbGVjdEl0ZW0 + DQogICAgPE11c3RGaWxsSXRlbT4wPC9NdXN0RmlsbEl0ZW0 + DQogIDwvRmllbGQ + DQogIDxGaWVsZCBOYW1lPSJ4dWV6aGkiIE9yZGVySUQ9IjE2IiBQYXJlbnRGaWVsZElEPSIwIiBHcm91cElEPSI2MiIgTWFuYWdlSXRlbT0iMCI + DQogICAgPERpc2FibGVkPnRydWU8L0Rpc2FibGVkPg0KICAgIDxGaWVsZEFsaWFzPuWtpuWItjwvRmllbGRBbGlhcz4NCiAgICA8VGlwcz4NCiAgICA8L1RpcHM + DQogICAgPEZpZWxkVHlwZT4xPC9GaWVsZFR5cGU + DQogICAgPEZpZWxkTGV2ZWw + MTwvRmllbGRMZXZlbD4NCiAgICA8RmllbGRXaWR0aD4xNjA8L0ZpZWxkV2lkdGg + DQogICAgPEZpZWxkSGVpZ2h0PjEwMDwvRmllbGRIZWlnaHQ + DQogICAgPEFsbG93RmlsZUV4dD4NCiAgICA8L0FsbG93RmlsZUV4dD4NCiAgICA8TWF4RmlsZVNpemU + DQogICAgPC9NYXhGaWxlU2l6ZT4NCiAgICA8RGVmYXVsdFZhbHVlPg0KICAgIDwvRGVmYXVsdFZhbHVlPg0KICAgIDxPcHRpb25zPg0KICAgIDwvT3B0aW9ucz4NCiAgICA8VG9vbEJhcj5CYXNpYzwvVG9vbEJhcj4NCiAgICA8SW5wdXRJdGVtPjE8L0lucHV0SXRlbT4NCiAgICA8Q29udHJpYnV0aW9uSXRlbT4xPC9Db250cmlidXRpb25JdGVtPg0KICAgIDxTZWFyY2hJdGVtPjA8L1NlYXJjaEl0ZW0 + DQogICAgPENvbGxlY3RJdGVtPjA8L0NvbGxlY3RJdGVtPg0KICAgIDxNdXN0RmlsbEl0ZW0 + MDwvTXVzdEZpbGxJdGVtPg0KICA8L0ZpZWxkPg0KICA8RmllbGQgTmFtZT0iYmVpemh1IiBPcmRlcklEPSIxNyIgUGFyZW50RmllbGRJRD0iMCIgR3JvdXBJRD0iNjIiIE1hbmFnZUl0ZW09IjAiPg0KICAgIDxEaXNhYmxlZD50cnVlPC9EaXNhYmxlZD4NCiAgICA8RmllbGRBbGlhcz7lpIfms6g8L0ZpZWxkQWxpYXM + DQogICAgPFRpcHM + DQogICAgPC9UaXBzPg0KICAgIDxGaWVsZFR5cGU + MTwvRmllbGRUeXBlPg0KICAgIDxGaWVsZExldmVsPjE8L0ZpZWxkTGV2ZWw + DQogICAgPEZpZWxkV2lkdGg + MTYwPC9GaWVsZFdpZHRoPg0KICAgIDxGaWVsZEhlaWdodD4xMDA8L0ZpZWxkSGVpZ2h0Pg0KICAgIDxBbGxvd0ZpbGVFeHQ + DQogICAgPC9BbGxvd0ZpbGVFeHQ + DQogICAgPE1heEZpbGVTaXplPg0KICAgIDwvTWF4RmlsZVNpemU + DQogICAgPERlZmF1bHRWYWx1ZT4NCiAgICA8L0RlZmF1bHRWYWx1ZT4NCiAgICA8T3B0aW9ucz4NCiAgICA8L09wdGlvbnM + DQogICAgPFRvb2xCYXI + QmFzaWM8L1Rvb2xCYXI + DQogICAgPElucHV0SXRlbT4xPC9JbnB1dEl0ZW0 + DQogICAgPENvbnRyaWJ1dGlvbkl0ZW0 + MTwvQ29udHJpYnV0aW9uSXRlbT4NCiAgICA8U2VhcmNoSXRlbT4wPC9TZWFyY2hJdGVtPg0KICAgIDxDb2xsZWN0SXRlbT4wPC9Db2xsZWN0SXRlbT4NCiAgICA8TXVzdEZpbGxJdGVtPjA8L011c3RGaWxsSXRlbT4NCiAgPC9GaWVsZD4NCjwvTW9kZWw + HgdNb2RlbElEBQExHg1JbnB1dEl0ZW1OYW1lBQlJbnB1dEl0ZW1kZAICDxYCHgtfIUl0ZW1Db3VudAICFgRmD2QWBGYPFQMCNTMM5Z + 65pys5L + h5oGvAjUzZAIBDxYCHwQCEBYgZg9kFgICAQ8PFhweDE11c3RGaWxsSXRlbQUBMB4JRmllbGRUeXBlBQEwHgdGaWVsZElEBQVUaXRsZR4HVG9vbEJhcgUFQmFzaWMeCkZpZWxkQWxpYXMFBuagh + mimB4MRGVmYXVsdFZhbHVlZR4HT3B0aW9ucwUFQmFzaWMeC0ZpZWxkSGVpZ2h0ZR4KRmllbGRXaWR0aAUDMzAwHwIFATEeDVBhcmVudEZpZWxkSUQFATAeCERpc2FibGVkBQR0cnVlHgRUaXBzZR4JSW5wdXRJdGVtBQExZGQCAQ9kFgICAQ8PFhwfBQUBMB8GBQEwHwcFCUF0dHJpYnV0ZR8IBQVCYXNpYx8JBQznibnmrorlsZ7mgKcfCgUHMDAwMDAwMR8LZR8MBQMxMDAfDQUDMjAwHwIFATEfDgUBMB8PBQR0cnVlHxBlHxEFATFkZAICD2QWAgIBDw8WHB8FBQExHwYFATAfBwUHQ2xhc3NJRB8IBQVCYXNpYx8JBQzmiYDlsZ7moI / nm64fCmUfC2UfDAUDMTAwHw0FAzIwMB8CBQExHw4FATAfDwUEdHJ1ZR8QZR8RBQExZGQCAw9kFgICAQ8PFhwfBQUBMB8GBQEwHwcFB1R1cm5VcmwfCAUFQmFzaWMfCQUM6L2s5ZCR6ZO + 5o6lHwplHwtlHwwFAzEwMB8NBQMzNTAfAgUBMR8OBQEwHw8FBHRydWUfEGUfEQUBMWRkAgQPZBYCAgEPDxYcHwUFATAfBgUBMB8HBQdLZXlUYWdzHwgFBUJhc2ljHwkFDeWFs + mUruWtl1RBR1MfCmUfC2UfDAUDMTAwHw0FAzIwMB8CBQExHw4FATAfDwUFZmFsc2UfEGUfEQUBMWRkAgUPZBYCAgEPDxYcHwUFATAfBgUBMB8HBQhDb3B5RnJvbR8IBQVCYXNpYx8JBQbmnaXmupAfCmUfC2UfDAUDMTAwHw0FAzIwMB8CBQExHw4FATAfDwUFZmFsc2UfEGUfEQUBMWRkAgYPZBYCAgEPDxYcHwUFATAfBgUBMB8HBQZBdXRob3IfCAUFQmFzaWMfCQUG5L2c6ICFHwplHwtlHwwFAzEwMB8NBQMyMDAfAgUBMR8OBQEwHw8FBHRydWUfEGUfEQUBMWRkAgcPZBYCAgEPDxYcHwUFATEfBgUBMB8HBQdBZGREYXRlHwgFBUJhc2ljHwkFDOabtOaWsOaXtumXtB8KZR8LZR8MBQMxMDAfDQUDMjAwHwIFATEfDgUBMB8PBQR0cnVlHxBlHxEFATFkZAIID2QWAgIBDw8WHB8FBQEwHwYFATAfBwUFSW50cm8fCAUFQmFzaWMfCQUM566A6KaB5LuL57uNHwplHwtlHwwFAzEwMB8NBQMyMDAfAgUBMR8OBQEwHw8FBHRydWUfEGUfEQUBMWRkAgkPZBYCAgEPDxYcHwUFATEfBgUBMB8HBQdDb250ZW50HwgFBUJhc2ljHwkFDOWFt + S9k + WGheWuuR8KZR8LZR8MBQMxMDAfDQUDMjAwHwIFATEfDgUBMB8PBQR0cnVlHxBlHxEFATFkZAIKD2QWAgIBDw8WHB8FBQEwHwYFATAfBwUKRGVmYXVsdFBpYx8IBQVCYXNpYx8JBQnnvKnnlaXlm74fCmUfC2UfDAUDMTAwHw0FAzM1MB8CBQExHw4FATAfDwUEdHJ1ZR8QZR8RBQExZGQCCw9kFgICAQ8PFhwfBQUBMB8GBQIxMB8HBRfpppbpobXnvKnnlaXlm74xMzgweDQ2MB8IBQVCYXNpYx8JBTPpppbpobXnvKnnlaXlm74xMzgweDQ2MC3pnZ7kuLvnq5nnrqHnkIbml6DpnIDkuIrkvKAfCmUfC2UfDAUDMTAwHw0FAzM1MB8CBQExHw4FATAfDwUEdHJ1ZR8QZR8RBQExZGQCDA9kFgICAQ8PFhwfBQUBMB8GBQEwHwcFCFByaW9yaXR5HwgFBUJhc2ljHwkFCeS8mOWFiOe6px8KZR8LZR8MBQMxMDAfDQUCNTAfAgUBMR8OBQEwHw8FBWZhbHNlHxBlHxEFATFkZAIND2QWAgIBDw8WHB8FBQEwHwYFATAfBwUESGl0cx8IZR8JBQnngrnlh7vmlbAfCmUfC2UfDAUDMTAwHw0FAjUwHwIFATEfDgUBMB8PBQR0cnVlHxBlHxEFATFkZAIOD2QWAgIBDw8WHB8FBQEwHwYFATAfBwUEQXJlYR8IBQVCYXNpYx8JBQzpgInmi6nln47luIIfCmUfC2UfDAUDMTAwHw0FAzIwMB8CBQExHw4FATAfDwUFZmFsc2UfEGUfEQUBMWRkAg8PZBYCAgEPDxYcHwUFATAfBgUBMB8HBQdJbnB1dGVyHwgFBUJhc2ljHwkFCeW9leWFpeiAhR8KZR8LZR8MBQMxMDAfDQUDMjAwHwIFATEfDgUBMB8PBQR0cnVlHxBlHxEFATFkZAIBD2QWBGYPFQMCNjIM5LiT5Lia6K6 + 572uAjYyZAIBDxYCHwQCAxYGZg9kFgICAQ8PFhwfBQUBMB8GBQExHwcFBmxlaWJpZR8IBQVCYXNpYx8JBQznlJ / mupDnsbvliKsfCmUfC2UfDAUDMTAwHw0FAzE2MB8CBQExHw4FATAfDwUEdHJ1ZR8QZR8RBQExZGQCAQ9kFgICAQ8PFhwfBQUBMB8GBQExHwcFBnh1ZXpoaR8IBQVCYXNpYx8JBQblrabliLYfCmUfC2UfDAUDMTAwHw0FAzE2MB8CBQExHw4FATAfDwUEdHJ1ZR8QZR8RBQExZGQCAg9kFgICAQ8PFhwfBQUBMB8GBQExHwcFBmJlaXpodR8IBQVCYXNpYx8JBQblpIfms6gfCmUfC2UfDAUDMTAwHw0FAzE2MB8CBQExHw4FATAfDwUEdHJ1ZR8QZR8RBQExZGQCBA8WAh4HVmlzaWJsZWhkAgYPEGQQFQIJ5b6F5a6h5qC4DOWuoeaguOmAmui / hxUCATABMRQrAwJnZ2RkAhAPEA9kFgIeB29uY2xpY2sFC3Nob3dHcm91cCgpZGRkAhEPFgIeCWlubmVyaHRtbAWoBDx0YWJsZSB3aWR0aD0iMTAwJSIgYWxpZ249ImNlbnRlciIgYm9yZGVyPSIwIj48dHI + PHRkIHdkaXRoPScyMCUnPjxsYWJlbD48aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9J0Fyckdyb3VwSUQnIHZhbHVlPScxJz7nvZHnq5nnrqHnkIblkZg8L2xhYmVsPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwvdGQ + PHRkIHdkaXRoPScyMCUnPjxsYWJlbD48aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9J0Fyckdyb3VwSUQnIHZhbHVlPScyJz7kuKrkurrkvJrlkZg8L2xhYmVsPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwvdGQ + PHRkIHdkaXRoPScyMCUnPjxsYWJlbD48aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9J0Fyckdyb3VwSUQnIHZhbHVlPSczJz7kvIHkuJrkvJrlkZg8L2xhYmVsPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwvdGQ + PHRkIHdkaXRoPScyMCUnPjxsYWJlbD48aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9J0Fyckdyb3VwSUQnIHZhbHVlPSc0Jz7nlKjmiLc8L2xhYmVsPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwvdGQ + PC90cj48L3RhYmxlPmQCKg8QD2QWAh8TBRFzaG93UEtUaW1lTGltaXQoKWRkZAItD2QWAmYPD2QWAh8TBRNyZXR1cm4oQ2hlY2tGb3JtKCkpZGRYYL1NKmWiBj9FxQ7eanRNTDBmGg ==',
    '__VIEWSTATEGENERATOR': 'EC691A77',
    'PreTitle': '',
    'Title': 'hahah',
    'TitleFontColor': '',
    'RefreshTF': '1',
    'ShowOn3G': '1',
    'Attribute7': '1',
    'm0': '1128',
    'm1128': '1151',
    'm1151': '1153',
    'ClassID': '1152',
    'Author': ',',
    'SelAuthor': '',
    'AddDate': '2017/4/18 22:01:16',
    'autointro': '1',
    'Intro': '',
    'AttachmentCharge': '0',
    'AttachmentChargeOnce': '1',
    'Content': '',
    'PageTitle': '',
    'DefaultPic': '',
    '首页缩略图1380x460': '',
    'Hits': '0',
    'Inputer': '',
    'leibie': '',
    'xuezhi': '',
    'beizhu': '',
    'ctl00$KSContent$TxtInputer': 'sxfu_ysgc',
    'ctl00$KSContent$Verify': '1',
    'templateflag': '2',
    'ctl00$KSContent$TemplateFile': '',
    'ctl00$KSContent$Template3GFile': '',
    'filetype': '0',
    'ctl00$KSContent$FileName': '',
    'ctl00$KSContent$HidFileName': '',
    'ctl00$KSContent$TxtSeoTitle': '',
    'ctl00$KSContent$TxtSeoKeyWords': '',
    'ctl00$KSContent$TxtSeoDescription': '',
    'ctl00$KSContent$InfoPurview': '0',
    'ctl00$KSContent$ReadPoint': '0',
    'ctl00$KSContent$ChargeType': '0',
    'PitchTime': '12',
    'ReadTimes': '10',
    'ctl00$KSContent$DividePercent': '0',
    'ctl00$KSContent$Subject': '',
    'ctl00$KSContent$VoteType': '1',
    'vote_num': '1',
    'editnum': '8',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'itemid': '0',
    'item': '',
    'votenum': '0',
    'ctl00$KSContent$BeginDate': '2017/4/18 22:01:16',
    'ctl00$KSContent$ExpireDate': '2017/4/18 22:01:16',
    'ctl00$KSContent$UserTF': '1',
    'ctl00$KSContent$LimitIP': '1',
    'ctl00$KSContent$hidVoteID': '0',
    'ctl00$KSContent$hidPKID': '0',
    'ctl00$KSContent$TxtPkTitle': '',
    'ctl00$KSContent$TxtPKZFGD': '',
    'ctl00$KSContent$TxtPKFFGD': '',
    'ctl00$KSContent$TxtPKZFVotes': '0',
    'ctl00$KSContent$TxtPKFFVotes': '0',
    'ctl00$KSContent$TxtPKSFVotes': '0',
    'ctl00$KSContent$RdbPKUserTF': '1',
    'ctl00$KSContent$RdbPKOnceTF': '0',
    'ctl00$KSContent$RdbPKVerifyTF': '0',
    'ctl00$KSContent$RdbPKStatus': '1',
    'ctl00$KSContent$RdbPKTimeLimit': '0',
    'ctl00$KSContent$TxtPKTBeginDate': '2017/4/18 22:01:15',
    'ctl00$KSContent$TxtPKTEndDate': '2017/5/18 22:01:15',
    'ctl00$KSContent$Foot1$submitbutton': '确定保存(O)',
    'ctl00$KSContent$Foot1$ID': '0'

}

cookies1={
    'Cookie':'UM_distinctid=15aeb27fa3931c-0708303a3db19f-293e1d4e-100200-15aeb27fa3a659; CNZZDATA1259721222=1028402859-1488032382-http%253A%252F%252F10.10.1.253%252F%7C1489999788; ASP.NET_SessionId=rvuuhe0ic3r2t5mxsvo0bz5m; myShop=userName=mgbry52ap0uo; Admin=AdminID=89&AdminUser=sxfu_ysgc&AdminPass=ab8227eb74568201&UserType=0&Role=3&DocPower=0&AdminLoginCode='
}

def get2(pn):#内页爬取
    url1='http://news.meishujia.cn/?act=app&appid=4115&mid=%d&p=view'%pn#原创新闻
    #url1 = "http://news.meishujia.cn/?act=app&appid=4096&mid=%d&p=view" % pn#综合类
    html1=requests.get(url1)
    html1.encoding = 'gbk'      #网页编码定义
    h2=html1.text


    reg2=r'<h1>(.*?)</h1>'       #取出标题
    title = re.findall(reg2, h2)


    reg2 = r'src="(.*?).jpg"'  # 取出标题
    photourl = re.findall(reg2, h2)



    reg2=r'''<ul class="nw_r_b nw_r_bt">
(.*?)<ul class="nw_r_ed">'''
    reg2 = re.compile(reg2, re.S)#re.S可匹配多行#编译正则表达式
    body = re.findall(reg2, h2)
    return url1,title,body,photourl

def login(payload):
    url1='http://www.sxfu.org/guanli/login.aspx'
    html1 = requests.post(url1,data=payload)

    headers1=html1.headers
    cookies=html1.cookies
    return  headers1

def fabu(pp,cookies1):
    #url1 = 'http://www.sxfu.org/guanli/Content/ks.content.aspx?Action=Add&Channelid=1'
    url1 = 'http://www.sxfu.org/guanli/Content/KS.Content.aspx?ChannelID=1&Action=Add&ClassID=1153'
    response = requests.post(url1,cookies=cookies1,data=pp,)
    returen_page=response.text
    return returen_page


if __name__=='__main__':
    #loginpage=login(payload)#登陆首页，本来想爬取cookies但是爬不到


    for i in range(3326, 3329):
        print('正在爬取编号%d文章'%i)
        url1, title, body,photostart = get2(i)
        # photourl=photostart[1]+'.jpg'
        # print(type(body))   #list
        # print(url1)
        # print(title)
        # print(body)
        # print(photourl)
        # # 'DefaultPic': '',  #缩略图
        # print('正在发布编号%d文章' % i)
        # pp['Title'] = title         #标题
        # pp['Content'] = body        #正文
        # pp['AddDate'] = '2017/4/18 22:01:16'
        # pp['DefaultPic']=photourl
        # #fabu(pp, cookies1)
        # print('发布完毕')
        # time.sleep(1)
        # break

        if len(title)!=0:
            if len(body)!=0:
                #print(type(body))   #list
                print(url1)
                print(title)
                print(body)
                #'DefaultPic': '',  #缩略图
                print('正在发布编号%d文章'%i)
                pp['Title']=title
                pp['Content']=body
                pp['AddDate']='2017/4/18 22:01:16'
                fabu(pp, cookies1)
                print('发布完毕')
                time.sleep(1)

            else:
                print('文章内容抓取失败')
                print(url1)
                print(title)
                continue
            #break
        else:
            print('标题抓取失败')
            print(url1)
            continue





