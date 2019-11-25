"""
发送文件给服务器
"""

import socket
from time import sleep

# 用于找到文件位置
path = ""
fileName = "desktop.png"

# host = '192.168.174.133'
host = "127.0.0.1"
port = 9678

def main():
    client = socket.socket()
    client.connect((host,port))
    client.send(fileName.encode(encoding="utf-8")) # 发送文件名
    sleep(2) # 等待2秒
    is_ac = client.recv(1024).decode(encoding="utf-8") # 是否ack
    if is_ac == "ACK":  # 发送数据
        fp = path+fileName
        with open(fp,"rb") as fr:
            data = fr.read()
            client.send(data)
    pass


if __name__ == "__main__":
    main()
