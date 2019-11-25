
import socket
import io
from PIL import ImageGrab
import base64

update_time = 30
html = """HTTP/1.1 200 OK
Content-Type: text/html

<html>
<meta http-equiv="refresh" content="{}">
<head>
<title>Desktop</title>
</head>
<body>
<figure>
    <figcaption>Desktop</figcaption>
    <img src="desktop.bmp" alt="desktop">
</figure>
</body>
</html>
""".format(update_time)

image_rep = """HTTP/1.1 200 OK
Content-Type: image/bmp


"""


def main():
    host = "127.0.0.1"
    port = 9678
    server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((host,port))
    server.listen(512)
    print("The server is Listenning ...")

    while True:
        client,addr = server.accept()
        request = client.recv(1024)
        request = str(request,encoding='utf-8')
        print(f"Current client is {addr} and the request is {request}")
        # print(request)
        if 'GET /desktop.bmp HTTP/1.1' in request:
            # imbuffer = io.BytesIO()
            imdesktop = ImageGrab.grab()
            imdesktop.save("desktop.bmp",format="bmp")
            imcontents = bytes()
            with open("desktop.bmp",'rb') as fr:
                imcontents = fr.read()
            # imdesktop.show() 可以截屏
            # imdesktop.save(imbuffer,'bmp')
            # imcontents = imbuffer.getvalue()
            # imbuffer.close()
            client.sendall(bytes(image_rep,encoding='utf-8')+imcontents)
        elif 'GET / HTTP/1.1' in request:
            client.sendall(bytes(html,encoding='utf-8'))
        else:
            client.sendall(bytes("HTTP/1.0 404 Not found\r\n",encoding='utf-8'))
        client.close()
    pass

if __name__ == "__main__":
    main()
