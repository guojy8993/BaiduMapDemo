#author guojingyu
#date      Sep 18, 2014
import eventlet
def handle(client):
    while True:
        c = client.recv(1024)
        print c
        client.sendall(c)

server = eventlet.listen(('0.0.0.0',7000))
pool = eventlet.GreenPool(20)
while True:
    new_sock,address = server.accept()
    pool.spawn_n(handle,new_sock)

# 0.0.0.0 as default value of localhost
#    
    
    
    