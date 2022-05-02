import socket
import threading
import json
import time
from cmd import Cmd


class Client(Cmd):
    """
    客户端
    """
    prompt = ''
    intro = '简易的python聊天小程序\n' + '输入help可以获取指令目录\n'

    def __init__(self):
        """
        构造函数
        """
        super().__init__()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__id = None
        self.__nickname = None
        self.__isLogin = False

    
    def __send_message_thread(self, message):
        """
        发送消息线程
        param message: 消息内容
        """
        self.__socket.send(json.dumps({
            'type': 'broadcast',
            'sender_id': self.__id,
            'message': message
        }).encode())

    

    def __receive_message_thread(self):
            """
            接受消息线程
            """
            while self.__isLogin:
                try:
                    buffer = self.__socket.recv(1024).decode()
                    obj = json.loads(buffer)
                    print('[' + str(obj['sender_nickname']) + '(' + str(obj['sender_id']) + ')' + ']', obj['message'])
                except Exception:
                    print('[Client] 无法从服务器获取数据')

    def start(self):
            """
            启动客户端
            """
            self.__socket.connect(('127.0.0.1',1919))
            self.cmdloop()
            
    def do_login(self, args):
        """
        登录聊天室
        param args: 登录的用户名
        """
        nickname = args.split(' ')[0]

        # 将昵称发送给服务器，获取用户id
        self.__socket.send(json.dumps({
            'type': 'login',
            'nickname': nickname
        }).encode())
        try:
            buffer = self.__socket.recv(1024).decode()
            obj = json.loads(buffer)
            if obj['id']:
                self.__nickname = nickname
                self.__id = obj['id']
                self.__isLogin = True
                print('[Client] 成功登录到聊天室')
                # 开启子线程用于接受数据
                thread = threading.Thread(target=self.__receive_message_thread)
                thread.setDaemon(True)
                thread.start()
            else:
                print('[Client] 无法登录到聊天室')
        except Exception:
            print('[Client] 无法从服务器获取数据')

    def do_logout(self, args=None):
        """
        登出聊天室
        """
        self.__socket.send(json.dumps({
            'type': 'logout',
            'sender_id': self.__id
        }).encode())
        self.__isLogin = False
        return True


    def do_send(self, args):
        """
        发送消息
        param args: 发送的内容
        """
        message = args
        # 显示自己发送的消息
        print('[' + str(self.__nickname) + '(' + str(self.__id) + ')' + ']', message)
        # 开启子线程用于发送数据
        thread = threading.Thread(target=self.__send_message_thread, args=(message,))
        thread.setDaemon(True)
        thread.start()



    def do_help(self, arg):
        """
        帮助
        :param arg: 参数
        """
        command = arg.split(' ')[0]
        if command == '':
            print('[Help] login nickname - 登录到聊天室，nickname是你选择的昵称')
            print('[Help] send message - 发送消息，message是你输入的消息')
            print('[Help] logout - 退出聊天室')
            print('author: 宋致远')
        elif command == 'login':
            print('[Help] login nickname - 登录到聊天室，nickname是你选择的昵称')
        elif command == 'send':
            print('[Help] send message - 发送消息，message是你输入的消息')
        elif command == 'logout':
            print('[Help] logout - 退出聊天室')
        else:
            print('[Help] 没有查询到你想要了解的指令')
