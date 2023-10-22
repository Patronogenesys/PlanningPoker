# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('127.0.0.1', 3000))
listener.listen(10)
print("listening")

speaker, address = listener.accept()
data = speaker.recv(1024).decode("utf-8")
print(data)
HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
content = "HI".encode("utf-8")
speaker.send(HDRS.encode('utf-8') + content)
print("stop")
