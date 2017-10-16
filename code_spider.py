import requests

import tools
import session_spider


class CodeSpider:
    def __init__(self):
        self.__session_spider_data__ = session_spider.SessionSpider().run()
        self.__session__ = self.__session_spider_data__.get('session')
        self.__view_state__ = self.__session_spider_data__.get('view_state')
        self.__path__ = tools.path + "/" + self.__session__ + ".gif"
        self.__web_path__ = "/auth/image/"+self.__session__
        self.__reault__ = {
            'session': self.__session__,
            'path': self.__web_path__,
            'view_state': self.__view_state__
        }
        self.__url__ = "http://202.116.160.170/CheckCode.aspx"
        self.__header__ = {
            "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",
            "Host":"202.116.160.170",
            "Referer":"http://202.116.160.170/"
        }
        self.__cookie__ = {
            "ASP.NET_SessionId" :self.__reault__.get("session")
        }

    def run(self):
        resp = requests.get(self.__url__, headers=self.__header__, cookies = self.__cookie__)
        print(self.__cookie__)
        if resp.status_code == 200:
            f = open(self.__path__, "wb")
            f.write(resp.content)
            f.close()
            return self.__reault__


if __name__ == '__main__':
    print(CodeSpider().run())