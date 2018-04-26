from http.server import BaseHTTPRequestHandler, HTTPServer
from webServer import webServer
class classServer:
    def __init__(self, *args, **kwargs):
        
        port = 1995
        server = HTTPServer(('',port),webServer)
        print("Web server running at : ",port)
        server.serve_forever()

if __name__=='__main__':
    server = classServer()