import queue, zerorpc
from auth.tools import Singleton
from auth.config import *
import pymysql

def connect():
    conn = pymysql.connect(host=db_host, port=db_port, user=db_user, password=db_password, db=db_database, charset='utf8')
    cursor = conn.cursor()
    return (conn, cursor)


def disconnect(conn, cursor):
    conn.close()
    cursor.close()


def get_user_db(conn, cursor, uid):

    sql = "select uid from user where uid = %d" %(uid)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as e:
        pass
    return result


def insert_auth_stu(conn, cursor, stu_num, stu_name):
    sql = "INSERT INTO scau_auth_user(stu_num, stu_name) VALUES (%s, %s)"
    cursor.execute(sql, (stu_num, stu_name))
    conn.commit()
    auth_id = cursor.lastrowid
    return auth_id


def update_user_auth(conn, cursor, uid, auth_id):
    sql = "UPDATE user SET auth = %d WHERE uid = %d" %(auth_id, uid)
    cursor.execute(sql)
    conn.commit()


class RPCServer(metaclass=Singleton):

    def __init__(self):
        self._auth_data = queue.Queue()

    def send_auth_data(self, auth_data):
        print(auth_data)
        stu_name = auth_data.get('name')
        stu_num = auth_data.get('number')
        uid = auth_data.get('uid')
        self._auth_data.put(auth_data, True)
        print("send auth data success")
        print(self._auth_data.qsize())
        conn, cursor = connect()
        result = get_user_db(conn, cursor, int(uid))
        if result != None:
            auth_id = insert_auth_stu(conn, cursor,stu_num, stu_name)
            if auth_id != None:
                update_user_auth(conn, cursor, int(uid), int(auth_id))
                disconnect(conn, cursor)
                return {
                    "stu_name": stu_name,
                    "stu_num": stu_num,
                    "uid": uid
                }





    def get_all_data(self):
        print(self._auth_data)


s = zerorpc.Server(RPCServer())
s.bind("tcp://0.0.0.0:{port}".format(port=port))
s.run()


# insert_auth_stu(conn, cursor, "201527010324", "wususua")
