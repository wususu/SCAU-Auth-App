import requests
from bs4 import BeautifulSoup


class LoginSpider:

    def __init__(self, number, passwd, code, session, view_state):
        self._url = "http://202.116.160.170/default2.aspx"
        self._header = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 52.0.2743.116Safari / 537.36',
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
        }
        self._payload = {
            '__VIEWSTATE': view_state,
            'txtUserName': number,
            'TextBox2': passwd,
            'txtSecretCode': code,
            'RadioButtonList1': '学生',
            'Button1':'',
            'lbLanguage':'',
            'hidPdrs':'',
            'hidsc':'',
        }
        self._cookie = {
            "ASP.NET_SessionId": session
        }

    def run(self):
        resp = requests.post(self._url,data=self._payload, headers=self._header, cookies=self._cookie)
        if resp.status_code == 200:
            html = BeautifulSoup(resp.content,"html.parser")
            try:
                name_tag = html.find('span', id="xhxm")
                name = name_tag.text
                if name is not None:
                    return name
            except:
                pass
        return None


if __name__ == '__main__':
    bb = LoginSpider("201527010324", "wpj19960214", "bnhe", "kdf0raazxprnj355untzx4uu", "dDwtNTE2MjI4MTQ7Oz5gXe9/FvmCp4TSSLd1QQxdVAgCkA==").run()
    print(bb)