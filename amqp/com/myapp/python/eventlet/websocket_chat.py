#author guojingyu
#date      Sep 18, 2014
import os
import eventlet
from eventlet import wsgi
from eventlet import websocket

PORT = 7000
participants = set()

@websocket.WebSocketWSGI
def handle(ws):
    participants.add(ws) #collectct the corrent sockets 
    try:
        while True:
            m = ws.wait()
            if m is None:
                break
            for p in participants:
                p.send(m)
    finally:
        participants.remove(ws)

def dispatch(environ,start_response):
    if environ['PATH_INFO'] == '/chat':
        print 'someone talks: '
        #start_response('200 OK',[('content-type','text/html')])
        #html_path = os.path.join(os.path.dirname(__file__),'websocket_chat.html')
        #return [open(html_path).read()%{'port':PORT}]
        return handle(environ,start_response)
    else:
        start_response('200 OK',[('content-type','text/html')])
        html_path = os.path.join(os.path.dirname(__file__),'websocket_chat.html')
        return [open(html_path).read()%{'port':PORT}]

if __name__ == "__main__":
    listener = eventlet.listen(('127.0.0.1',PORT))
    print("\nVisit http://localhost:7000/ in your websocket-capable browser.\n")
    wsgi.server(listener,dispatch)
