########################################################################
#
# Twisted PJUSA main module
#
# 2012 - Ulrik Hoerlyk Hjort
########################################################################
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from threading import Thread
from twisted.web2 import server, http, resource, channel
from twisted.web2 import static, http_headers, responsecode

import sys
import ah_sip as sip


##########################################################################
#
# HTTP listener class
#
##########################################################################
class Http_Listener(Resource):

    isLeaf = True
    sip_handle = None


    def render_GET(self, request):
        
        response = "Success"

        if request.path == "/init_sip":
            self.sip_handle = sip.Sip(5080)            

        if request.path == "/register":
            if self.sip_handle == None:
                response = "Error: Sip not  initialized"
            else:
                response = self.sip_handle.register(request.args['domain'][0],request.args['username'][0],request.args['password'][0],5080)

        if request.path == "/disconnect":
            response = self.sip_handle.disconnect()
            self.sip_handle = None

        return response



##########################################################################
#
#
#
##########################################################################
def main():
    if len(sys.argv) != 2:
        print "Usage: " + sys.argv[0] + " http_port"
        exit(0)

    http_port = int(sys.argv[1])
    resource = Http_Listener()
    factory = Site(resource)
    reactor.listenTCP(http_port, factory)
    reactor.run()


if __name__ == "__main__":
    main()
