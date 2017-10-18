import zerorpc
from auth.tools import Singleton
from auth.config import *


class RCPClient(metaclass=Singleton):

    def __init__(self):
        self._client = zerorpc.Client()
        self._client.connect("tcp://{ip}:{port}".format(ip=ip,port=port))
        self._client.debug = True

    def send(self, auth_data):
        print(auth_data)
        return self._client.send_auth_data(auth_data)

    def disconnect(self):
        self._client.disconnect("tcp://{ip}:{port}".format(ip=ip,port=port))

