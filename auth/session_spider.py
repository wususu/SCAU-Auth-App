import requests
from bs4 import BeautifulSoup


class SessionSpider:

    def __init__(self):
        self._url = "http://202.116.160.170/"
        self._html = None

    def run(self):
        resp = requests.get(self._url)
        if resp.status_code == 200:
            session_id = resp.cookies.get("ASP.NET_SessionId")
            self._html = BeautifulSoup(resp.content, "html.parser")
            view_state = self._html.find('input', type="hidden").attrs['value']
            return {
                'session':session_id,
                'view_state':view_state
            }


if __name__ == '__main__':
    b = SessionSpider()
    b.run()