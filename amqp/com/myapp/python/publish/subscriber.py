#author guojingyu
#date      Sep 16, 2014
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',type='fanout')

queue = channel.queue_declare(exclusive=True) #shared with nobody else ,it will be deleted on the queue disconnected
queuename = queue.method.queue
channel.queue_bind(exchange='logs',queue=queuename) 

print "[*] Waiting for logs . To exit pressCtrl+C "
def callback(channel,method,properties,body):
    print "[x] %s"%body

channel.basic_consume(callback,queue=queuename,no_ack=True)
channel.start_consuming()
