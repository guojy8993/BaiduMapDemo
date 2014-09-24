#author guojingyu
#date      Sep 16, 2014
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello3',durable=True)

print "[*] Waiting for message .Toe exit press Ctrl+C "
def callback(channel,method,properties,body):
    print "[*] Received %s"%str(body)
    time.sleep(body.count("."))
    print "[*] Job Done ! And it takes %s seconds "%body.count(".")
    channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue='hello3')
channel.start_consuming()
