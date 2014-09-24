#author guojingyu
#date      Sep 16, 2014
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rabbitmq')

print '[*] Waiting for messages. To exit press Ctrl+C '

def callback(channel,method,properties,body):
    print '[*] body : %s'%body
channel.basic_consume(callback,queue='rabbitmq',no_ack=True)
channel.start_consuming()



