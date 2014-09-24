说明:如果client端输入的数值较大，那么计算fib会消耗大量时间，消息队列被阻塞 ;
使用 rabbitmqctl force-reset 重置节点，清空所有持久化消息 ;
for more info : sudo rabbitmqctl -h
=================================================================
在操作的过程造成rabbitmq-server程序的不完整:
比如 sudo rabbitmqctl delete_vhost ;
可以通过:
    sudo apt-get check rabbitmq-server #检查依赖
    sudo apt-get purge rabbitmq-server #彻底清除程序与配置残留
    ...
    sudo apt-get install rabbitmq-server #这样就修复了
=================================================================