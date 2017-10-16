import requests
from bs4 import BeautifulSoup

class LoginSpider:
    error= {
        "state": "error"
    }
    ok= {
        "state": "success",
        "name": None
    }
    def __init__(self, number, passwd, code, session, view_state):

        print("number: ",number )
        print("passed: ",passwd)
        print("code: ", code)
        print("session: ", session)
        print("view_state: ", view_state)
        self.__url__ = "http://202.116.160.170/default2.aspx"
        self.__header__ = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 52.0.2743.116Safari / 537.36',
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
        }
        self.__payload__ = {
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
        self.__cookie__ = {
            "ASP.NET_SessionId": session
        }



    def run(self):
        resp = requests.post(self.__url__,data=self.__payload__, headers=self.__header__, cookies=self.__cookie__)
        if resp.status_code == 200:
            html = BeautifulSoup(resp.content,"html.parser")
        try:
            # print(html)
            name_tag = html.find('span', id="xhxm")
            # print(name_tag)
            name = name_tag.text
            if name != None:
                self.ok["name"] = name
                return self.ok
        except:
            pass
        return self.error


if __name__ == '__main__':
    bb = LoginSpider("201527010324", "wpj19960214", "bnhe", "kdf0raazxprnj355untzx4uu", "dDwtNTE2MjI4MTQ7Oz5gXe9/FvmCp4TSSLd1QQxdVAgCkA==").run()
    print(bb)