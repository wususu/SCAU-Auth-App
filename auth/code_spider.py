import requests
from .config import *

from auth import session_spider


class CodeSpider:

    def __init__(self):
        self._session_spider_data = session_spider.SessionSpider().run()
        self._session = self._session_spider_data.get('session')
        self._view_state = self._session_spider_data.get('view_state')
        self._path = path + "/" + self._session + ".gif"
        self._web_path = "/auth/image/" + self._session
        self._reault = {
            'session': self._session,
            'path': self._web_path,
            'view_state': self._view_state
        }
        self._url = "http://202.116.160.170/CheckCode.aspx"
        self._header = {
            "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",
            "Host":"202.116.160.170",
            "Referer":"http://202.116.160.170/"
        }
        self._cookie = {
            "ASP.NET_SessionId" :self._reault.get("session")
        }

    def run(self):
        resp = requests.get(self._url, headers=self._header, cookies = self._cookie)
        if resp.status_code == 200:
            f = open(self._path, "wb")
            f.write(resp.content)
            f.close()
            return self._reault


if __name__ == '__main__':
    print(CodeSpider().run())