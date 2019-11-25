"""由于只能从电脑传输文件到服务器

所以服务端作为接受者 客户端作为发送者
"""
import socket
# import os
host = "127.0.0.1"
port = 9678
server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM) # 建立 IPV4 TCP 方式的服务端
server.bind((host,port)) # 绑定端口

def main():
    server.listen(512)
    print("Start Listening ... ")
    while True:
        client,addr = server.accept() # 客户端 和 地址
        print(f"Current client is {addr} ")
        fileName = client.recv(1024).decode(encoding="utf-8") # 得到名字
        print(f'Current file name is {fileName}')
        client.send("ACK".encode(encoding="utf-8")) # ACK
        in_data = bytes() # 开始接收文件
        data = client.recv(1024)
        while data:
            in_data += data
            data = client.recv(1024)
        with open(f"files/{fileName}",'wb') as fw: # 写入文件
            fw.write(in_data)
        client.close()
    pass


if __name__ == "__main__":
    main()








