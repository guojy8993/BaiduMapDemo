#author guojingyu
#date      Sep 17, 2014
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',type='topic')
result = channel.queue_declare(exclusive=True)
queue = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    print >> sys.stderr,"Using: %s [binding_key]..."%(sys.argv[0])
    sys.exit(1)
for key in binding_keys:
    channel.queue_bind(exchange='topic_logs',queue=queue,routing_key=key)
print "[*] Waiting for logs . To exit press Ctrl+C "

def callback(channel,method,properties,body):
    print "[x] %s:%s "%(method.routing_key,body)
channel.basic_consume(callback,queue=queue,no_ack=True)
channel.start_consuming()
