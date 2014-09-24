#author guojingyu
#date      Sep 17, 2014
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',type='topic')
routing_key = sys.argv[1] if len(sys.argv)>1 else 'anoymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello , this demo shows how to use a topic exchange !'
# python emit_log_topic.py  anoymous.info  'let me tell you the truth'
channel.basic_publish(exchange='topic_logs',routing_key=routing_key,body=message)
print "[*] Send %s:%s "%(routing_key,message)
connection.close()

