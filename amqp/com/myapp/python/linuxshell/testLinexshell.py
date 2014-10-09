#author guojingyu
#date      Sep 10, 2014

import utils as util
import re
if __name__=="__main__":
    
    #1.common utils
    arplocal = ['arp','192.168.12.1']
    '''
    echo = ['echo','hello']
    mkdir = ['mkdir','/home/cache']
    pinglocal = ['ping','192.168.1.1','-c','3']
    line_no_limit_ping = ['ping','192.168.1.1']
    shownetinfo = ['ifconfig']
    #findlog = ['find','/ ','-name','*.log','|','grep','dbus']
    findlog = [' find',' / ','-name','*.log',' | ','grep',' dbus']
    
    #2.service management utils
    startmq = ['service','rabbitmq-server','start']
    stopmq = ['service','rabbitmq-server','stop']
    restartmq = ['service','rabbitmq-server','restart']
    #3.iptables
    cutnet = [
                 'iptables','-h'
             ]
    
    #4.ovs
    ovs_h_2_file = ['ovs-vsctl','-h','>','/home/guojingyu/1.txt']
    # ovs-vsctl -h > /home/guojingyu/1.txt
    newbr = ['ovs-vsctl','add-br','br1000']
    listbr = ['ovs-vsctl','list-br']
    addport = ['ovs-vsctl','add-port','br1000','tap20140910pm0600']
    list_port_on_br = ['ovs-vsctl','list-ports','br1000']
    port_to_br = ['ovs-vsctl','port-to-br','tap20140910pm0600']
    list_ifaces = ['ovs-vsctl','list-ifaces','br1000']
    iface_to_br = ['ovs-vsctl','iface-to-br','tap20140910pm0600']
    br_to_vlan =  ['ovs-vsctl',' br-to-vlan ','br1000']
    #make sure cmd executed result has limited lines or will be blocked
    #password = 'Kuotsingyu0903!'
    #findlog = ['find','/','-name','*.log']
    #filterlog = ['|','grep','dbus']    
    #print findlog+filterlog
    #cmd = findlog+filterlog
    #env = {'password':password}
    #cmd = echo
    
    '''
    cmd = arplocal
    root_helper = 'sudo'
    res = util.execute(cmd=cmd,root_helper=root_helper)
    print res
    #typeof (res) = basestr
    print 'Cmd as follows:\n'+' '.join(cmd)+'\n\nOutput as folows:\n'+res
    
    lines = res.strip().split("\n")    
    titles = re.split("\s+",lines[0])
    body = [re.split("\s+",line) for line in lines[1:] if len(line)> 0]
    print body
    
    msg = ""
    for sub in body:
        for f in range(len(titles)):
            msg += titles[f-1]+" : "+sub[f-1]
            if f<len(titles)-1:
                msg += " && " 
        msg += "\n"
    print msg
    '''
    rmap = dict()
    for sub in body:
        for f in range(len(titles)):
            rmap.update({titles[f-1]:sub[f-1]})
    print rmap
    '''
    
    ins = raw_input("input:")
    print ins
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    