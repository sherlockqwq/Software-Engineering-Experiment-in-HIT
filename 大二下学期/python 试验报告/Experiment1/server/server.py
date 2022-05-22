import socket
import threading
import json


class Server:
    """
    服务器类
    """

    def __init__(self):

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connections = list()
        self.__nicknames = list()

    def __user_thread(self, user_id):
        """
        用户子线程
        """
        connection = self.__connections[user_id]
        nickname = self.__nicknames[user_id]
        print('[Server] 用户', user_id, nickname, '加入聊天室')
        self.__broadcast(message='用户 ' + str(nickname) + '(' + str(user_id) + ')' + '加入聊天室')

        while True:
            try:
                buffer = connection.recv(1024).decode()
                # 解析成json数据
                obj = json.loads(buffer)
                # 如果是广播指令
                if obj['type'] == 'broadcast':
                    self.__broadcast(obj['sender_id'], obj['message'])
                elif obj['type'] == 'logout':
                    print('[Server] 用户', user_id, nickname, '退出聊天室')
                    self.__broadcast(message='用户 ' + str(nickname) + '(' + str(user_id) + ')' + '退出聊天室')
                    self.__connections[user_id].close()
                    self.__connections[user_id] = None
                    self.__nicknames[user_id] = None
                    break
                else:
                    print('[Server] 无法解析json数据包:', connection.getsockname(), connection.fileno())
            except Exception:
                print('[Server] 连接失效:', connection.getsockname(), connection.fileno())
                self.__connections[user_id].close()
                self.__connections[user_id] = None
                self.__nicknames[user_id] = None

    def __broadcast(self, user_id=0, message=''):

        #广播
        for i in range(1, len(self.__connections)):
            if user_id != i and self.__connections[i]:
                self.__connections[i].send(json.dumps({
                    'sender_id': user_id,
                    'sender_nickname': self.__nicknames[user_id],
                    'message': message
                }).encode())

    def __waitForLogin(self, connection):
        try:
            buffer = connection.recv(1024).decode()
            # 解析成json数据
            obj = json.loads(buffer)
            if obj['type'] == 'login':
                self.__connections.append(connection)
                self.__nicknames.append(obj['nickname'])
                connection.send(json.dumps({
                    'id': len(self.__connections) - 1
                }).encode())
                # 开辟一个新的线程
                thread = threading.Thread(target=self.__user_thread, args=(len(self.__connections) - 1,))
                thread.setDaemon(True)
                thread.start()
            else:
                print('[Server] 无法解析json数据包:', connection.getsockname(), connection.fileno())
        except Exception:
            print('[Server] 无法接受数据:', connection.getsockname(), connection.fileno())

    def start(self):

        self.__socket.bind(('127.0.0.1', 1919))

        self.__socket.listen(10)
        print('[Server] 服务器正在运行......')


        self.__connections.clear()
        self.__nicknames.clear()
        self.__connections.append(None)
        self.__nicknames.append('System')


        while True:
            connection, address = self.__socket.accept()
            print('[Server] 收到一个新连接', connection.getsockname(), connection.fileno())

            thread = threading.Thread(target=self.__waitForLogin, args=(connection,))
            thread.setDaemon(True)
            thread.start()
