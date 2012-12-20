########################################################################
#
# Inter-Process Communication module
#
# 2012 - Ulrik Hoerlyk Hjort
########################################################################
from Queue import Queue
from threading import Thread
import time

class Task(Thread):
   def __init__ (self):
      Thread.__init__(self)
   def run(self):
      while 1:
          print "running"
          time.sleep(1)

class Mailbox:
    def __init__(self):
        self.mailbox = Queue()

    def send(self, message, sender):
        self.mailbox.put((message, sender), block = False)

    def receive(self, timeout = None):
        return self.mailbox.get(block = True, timeout = timeout)




#mailbox = Mailbox()

#while True:
#    mailbox.send((1,2,3,"qwe"),"qwe1")
#    print "recv: ",mailbox.receive(timeout=None)[0][0]
#    print "recv: ",mailbox.receive(timeout=None)
