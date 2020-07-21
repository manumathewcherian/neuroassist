import socket;

PORT = 13854
IP = '127.0.0.1'

s=socket.socket()
s.connect((IP,PORT))
st = "{ \"enableRawOutput\" : true, \"format\" : \"Json\" }"
s.send(st.encode())

while True:
    st = s.recv(2048).decode()
    print(st)
s.close()