# -*- coding: utf-8 -*-
import asyncore
import sys
import tkinter as tk

class EchoClient(asyncore.dispatcher_with_send):
    def __init__(self,message):
        asyncore.dispatcher_with_send.__init__(self)
        self.message = message
        self.create_socket()
        
    def handle_write(self):
        self.send(self.message.encode('utf-8'))
        
    def handle_read(self):
        data = self.recv(8192)
        print(data.decode('utf-8'))
        self.close()
        
    def handle_close(self):
        sys.exit(0)
        

class EchoView(tk.Frame):
    """Echo クライアントユーザーインターフェース"""
    def __init__(self,master):
        super(EchoView,self).__init__(master)
        self.listcontainer = tk.Frame(self)
        self.listbox = tk.Listbox(self.listcontainer)
        self.yscroll = tk.Scrollbar(self.listcontainer)
        self.listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.yscroll.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        self.listcontainer.pack(expand=True, fill=tk.BOTH)
        
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.BOTTOM, expand=True, fill=tk.X)

def idle_task(root):
    try:
        asyncore.loop(count=1,timeout=1)
    finally:
        root.after(200,functools.partial(idle_task,root))
        
def main():
    root = tk.Tk()
    root.after(200,functools.partial(idle_task,root))
    view = EchoView(root)
    view.pack(expand=True,fill=tk.BOTH)
    client = EchoClient(view)
    client.connect(('localhost',8080))
    root.mainloop()
    
