#author guojingyu
#date      Sep 16, 2014
#This demo displays the publish/subscribe mode
#command: sudo rabbitmqctl -h (for more info about rabbitmq)

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',# LOG exchange as default one brocasts messages it receives
                         type='fanout'                         
                         )
message = ' '.join(sys.argv[1:]) or 'This Demo Shows how To Use Fanout Exchange'
channel.basic_publish(exchange='logs',routing_key='',body=message)
print "[*]Send %s "%message
connection.close()




'''
    $ sudo rabbitmqctl list_exchanges
    Listing exchanges ...
    logs      fanout
    amq.direct      direct
    amq.topic       topic
    amq.fanout      fanout
    amq.headers     headers
    ...done.
'''
'''
     result = channel.queue_declare() # let the server choose a random queue name for us
     result = channel.queue_declare(exclusive=True) # once we disconnect the consumer the queue should be deleted
     messages are routed to the queue with the name specified by routing_key, if it exists.
     
     binding(That relationship between exchange and a queue is called a binding.)
'''
