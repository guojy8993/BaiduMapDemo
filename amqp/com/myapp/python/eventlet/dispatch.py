#author guojingyu
#date      Sep 18, 2014
import eventlet
feedparser = eventlet.import_patched("feedparser")

pool = eventlet.GreenPool()
def fetch_title(url):
    d = feedparser.parse(url)
    return d.feed.get('title','')
def app(environ,start_response):
    pile = eventlet.GreenPile(pool)
    for url in environ('wsgi.input').readlines():
        pile.spawn(fetch_title,url)
    titles = ".".join(pile)
    start_response('200 OK',[('Content-type','text/plain')])
    return [titles]
        