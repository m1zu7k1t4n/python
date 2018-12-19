# -*- coding: utf-8 -*-
import socket
class BouyomiChan(object):
    def __init__(self, host="localhost", port=50001):
        self.host = host
        self.port = port

    def clear(self):
        self.command(self.host, self.port, 64)

    def pause(self):
        self.command(self.host, self.port, 16)

    def resume(self):
        self.command(self.host, self.port, 32)

    def skip(self):
        self.command(self.host, self.port, 48)

    def talk(self, message, volume=-1, speed=-1, tone=-1, voice=0):
        self._talk(self.host, self.port, volume, speed, tone, voice, message)

    def command(self, host, port, command):
        data = list()
        data.append(command & 0xFF)
        data.append((command >> 8) & 0xFF)
        self.send(self.host, self.port, data)

    def send(self, host, port, data):
        socket = None
        try:
            socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.connect((host, port))
            socket.send(data)
        except:
            print("接続できませんでした")
        finally:
            try:
                if socket != None:
                    socket.close()
            except Exception as e:
                print(e.args)

    def _talk(self, host, port, volume, speed, tone, voice, message):
        messageData = None
        try:
            messageData = [x for x in message.encode("utf-8")]
        except Exception as e:
            print(e.args)
        length = len(messageData)
        data = [0] * 15
        data[0]= 1
        data[1]= 0
        data[2]= ((speed >> 0) & 0xFF)
        data[3]= ((speed >> 8) & 0xFF)
        data[4]= ((tone >> 0) & 0xFF)
        data[5]= ((tone >> 8) & 0xFF)
        data[6]= ((volume >> 0) & 0xFF)
        data[7]= ((volume >> 8) & 0xFF)
        data[8]= ((voice >> 0) & 0xFF)
        data[9]= ((voice >> 8) & 0xFF)
        data[10]= 0
        data[11]= ((length >> 0) & 0xFF)
        data[12]= ((length >> 8) & 0xFF)
        data[13]= ((length >> 16) & 0xFF)
        data[14]= ((length >> 24) & 0xFF)
        data = data + messageData
        self.send(host, port, data)


if __name__ == '__main__':
    bouyomi = BouyomiChan()
    bouyomi.talk("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめも")



