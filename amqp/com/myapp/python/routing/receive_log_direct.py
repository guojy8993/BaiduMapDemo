#author guojingyu
#date      Sep 16, 2014
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_log',type='direct')

queue = channel.queue_declare()
queuename = queue.method.queue

severities = sys.argv[1:]
if not severities:
    print >> sys.stderr , "Using %s  [info][error][waring]"%(sys.argv[0])
    sys.exit(1)
for severity in severities:
    channel.queue_bind(exchange='direct_log',queue=queuename,routing_key=severity)
print '[*] Waiting For Logs .To exit press Ctrl + C'

def callback(channel,method,properties,body):
    print "[x] %s:%s "%(method.routing_key,body)

channel.basic_consume(callback,queue=queuename,no_ack=True)
channel.start_consuming()