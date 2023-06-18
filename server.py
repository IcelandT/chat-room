# -*- coding: utf-8 -*-
import socket
import threading
import multiprocessing


class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 9989
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 聊天室所有用户
        self.user_list = list()

    def start(self):
        """
        开启聊天室
        :return:
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"{self.host}:{self.port}服务已开启.")

        while True:
            client, address = self.server_socket.accept()
            user = {'socket': client, 'address': address}

            threading.Thread(target=self.handle_client, args=(user, )).start()

    def handle_client(self, user):
        """
        处理事件
        :return:
        """
        socket = user["socket"]
        while True:
            try:
                message = socket.recv(1024).decode('utf-8')
                if "name=" in message:
                    user_name = message.split("=")[1]
                    message = f"[!] {user_name} 加入了群聊!"
                    print(message)

                    user.update({"name": user_name})
                    self.user_list.append(user)

                print(message)
                self.broadcast(message)

            except Exception as e:
                message = f"[!] {user['name']} 离开了群聊!"
                self.broadcast(message, socket)
                self.disconnect_user(user)
                break

    def broadcast(self, message, socket=None):
        """
        广播
        :param message:
        :param socket:
        :return:
        """
        for user in self.user_list:
            if socket:
                if user["socket"] != socket:
                    try:
                        user["socket"].sendall(message.encode("utf-8"))
                        self.send_online_user_nums(user["socket"])
                    except Exception as e:
                        self.disconnect_user(user)
                        self.send_online_user_nums(user["socket"])
            else:
                try:
                    user["socket"].sendall(message.encode("utf-8"))
                    self.send_online_user_nums(user["socket"])
                except Exception as e:
                    self.disconnect_user(user)
                    self.send_online_user_nums(user["socket"])

    def send_online_user_nums(self, socket):
        """
        发送在线人数
        :return:
        """
        socket.sendall(f"9000:{self.user_list}".encode("utf-8"))

    def disconnect_user(self, user):
        """
        断开用户连接
        :param user:
        :return:
        """
        message = f"[!] {user['name']} 离开了群聊!"
        print(message)
        user["socket"].close()
        self.user_list.remove(user)


if __name__ == '__main__':
    Server().start()