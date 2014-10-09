#author guojingyu
#date      Sep 10, 2014

import utils as util
import re
from Tkinter import *
import time


'''
root = Tk()
root.title("yw")
root.geometry("800x600")
menubar = Menu(root)

open_dict = {"label":"Open","command":test}
save_dict = {"label":"Save","command":reacts}
filemenu = Menu(menubar)
filemenu.add_command(open_dict)
filemenu.add_command(save_dict)
filemenu.add_separator()
menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)

root.mainloop()
'''
'''
root = Tk()
def callback(event):
    print event.x,event.y 

frame = Frame(root,width=100,height=100)
frame.bind("<Button-1>",callback)
frame.pack()

root.mainloop()
'''
def arp(event):
    arplocal = ['arp','192.168.12.1']
    cmd = arplocal
    root_helper = 'sudo'
    res = util.execute(cmd=cmd,root_helper=root_helper)
    
    lines = res.strip().split("\n")
    
    titles = re.split("\s+",lines[0]) 
    body = [re.split("\s+",line) for line in lines[1:] if len(line)> 0]

    rmap = dict()
    for sub in body:
        for f in range(len(titles)):
            rmap.update({titles[f-1]:sub[f-1]})
    print rmap

root = Tk()
frame = Frame(root,width=800,height=600)
frame.focus_set()
frame.bind("<Key-2>",arp)
frame.pack()
root.mainloop()

def reacts():
    print "33"

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    