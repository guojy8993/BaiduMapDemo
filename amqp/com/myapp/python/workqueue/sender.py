#author guojingyu
#date      Sep 16, 2014
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello3',durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello world'
#sys.argv : the parameter that we start this app with
#e.g : python sender.py yeah.... , hence , sys.argv = yeah....
channel.basic_publish(exchange='',
                      routing_key='hello3',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode = 2) # make msg persistent
                     )
print "[*] Send %s "%message
connection.close()

#attention : durable and delivery_mode to ensure message safety;

