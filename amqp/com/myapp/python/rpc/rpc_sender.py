#author guojingyu
#date      Sep 17, 2014
import pika
import sys
import uuid
class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,queue=self.callback_queue,no_ack=True)
    def on_response(self,ch,method,prop,body):
        if self.correlation_id == prop.correlation_id:
            self.response = body
    def call(self,n):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.correlation_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        print "[*] Client has received fib-computing result of %d : %s"%(n,self.response)
        
        #gc
        self.connection.close()
        self.connection = None

fibonacci_rpc_client = FibonacciRpcClient()
num = sys.argv[1] or 0
fibonacci_rpc_client.call(int(num))
        