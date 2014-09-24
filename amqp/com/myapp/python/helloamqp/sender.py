#author guojingyu
#date      Sep 16, 2014
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
queuename = channel.queue_declare(queue='rabbitmq')
print "[*] The newly declared queue named : %s"%queuename.method.queue
channel.basic_publish(exchange='',routing_key='rabbitmq',body='hello ip')
connection.close()

