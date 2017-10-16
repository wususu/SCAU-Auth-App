import requests
from bs4 import  BeautifulSoup


class SessionSpider:

    def __init__(self):
        self.__url__ = "http://202.116.160.170/"
        self.__html__ = None



    def run(self):
        resp = requests.get(self.__url__)
        if resp.status_code == 200:
            session_id = resp.cookies.get("ASP.NET_SessionId")
            self.__html__ = BeautifulSoup(resp.content, "html.parser")
            view_state = self.__html__.find('input', type="hidden").attrs['value']
            return {
                'session':session_id,
                'view_state':view_state
            }



if __name__ == '__main__':
    b = SessionSpider()
    b.run()