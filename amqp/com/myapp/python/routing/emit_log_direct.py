#author guojingyu
#date      Sep 16, 2014
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_log',type='direct')

severity = sys.argv[1] if len(sys.argv)>1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello world !'
channel.basic_publish(exchange='direct_log',routing_key=severity,body=message)
print "[*] Send %s:%s"%(severity,message) 
connection.close()

#multi-queue share the same exchange and routing key takes the job to dispatch messages from same exchange
#to different , corresponding queue ;

