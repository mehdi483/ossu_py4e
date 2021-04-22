import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('data.pr4e.org', 80))
s.send(b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n')

while True:
    data = s.recv(512)
    
    if len(data) < 1:
        break

    print(data.decode(), end='')

s.close()