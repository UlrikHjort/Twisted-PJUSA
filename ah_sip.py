########################################################################
#
# SIP handle module
#
# 2012 - Ulrik Hoerlyk Hjort
########################################################################
import sys
import pjsua as pj
import threading

######################################################
#
#
#
#
######################################################
def log_cb(level, str, len):
    print str,



######################################################
#
#
#
#
######################################################
class MyAccountCallback(pj.AccountCallback):
    sem = None


    ##################################################
    #
    #
    ##################################################
    def __init__(self, account):
        pj.AccountCallback.__init__(self, account)


    ##################################################
    #
    #
    ##################################################
    def wait(self):
        self.sem = threading.Semaphore(0)
        self.sem.acquire()

    ##################################################
    #
    #
    ##################################################
    def on_reg_state(self):
        if self.sem:
            if self.account.info().reg_status >= 200:
                self.sem.release()



######################################################
#
#
#
#
######################################################
class Sip():


    ##################################################
    #
    #
    ##################################################
    def __init__(self, port):
        self.lib  = pj.Lib()
        self.acc = None
        try:
            self.lib.init(log_cfg = pj.LogConfig(level=4, callback=log_cb))
            self.lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(port))
            self.lib.start()        
            
        except pj.Error, e:
            print "Exception: " + str(e)
            lib.destroy()


    ##################################################
    #
    # register sip client
    # INPUT: string: sip server address, 
    #        string: username, 
    #        string: password, 
    #        int:    sip port
    #
    # RETURNS: string: (status, reason)
    ##################################################
    def register(self,sip_server,username, password, port):

        try:
            acc = self.lib.create_account(pj.AccountConfig(sip_server, username, password))

            acc_cb = MyAccountCallback(acc)
            acc.set_callback(acc_cb)
            acc_cb.wait()

            return "" + str(acc.info().reg_status) + "," + acc.info().reg_reason
        except pj.Error, e:
            print "Exception: " + str(e)
            self.lib.destroy()



    ##################################################
    #
    # disconnect from server
    #    
    # INPUT: None
    #
    # RETURNS: None
    ##################################################
    def disconnect(self):
            self.lib.destroy()
            self.lib = None


    ##################################################
    #
    #
    ##################################################
    def destroy(self):
            self.lib.destroy()
            self.lib = None


    ##################################################
    #
    #
    ##################################################
    def __del__(self):
            self.lib.destroy()
            self.lib = None
