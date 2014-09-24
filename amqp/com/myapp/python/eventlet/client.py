#author guojingyu
#date      Sep 18, 2014
import eventlet
c = eventlet.connect(('127.0.0.1',7000))
while True:
    data = raw_input("Enter data:")
    c.sendall(data)
    rc = c.recv(1024)
    print rc
    
#client.py AND server.py