from http.server import BaseHTTPRequestHandler, HTTPServer

from urllib.parse import urlparse, parse_qs
import time
import json

hostName = "localhost"
hostPort = 9000

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        
        parsed_path = urlparse(self.path)
        print(parsed_path.path)
        print(parse_qs(parsed_path.query))
        
        response = {
            'status':'SUCCESS',
            'data':{
                '/aaa': self.do_aaa(parse_qs(parsed_path.query)),
                '/bbb': self.do_bbb(parse_qs(parsed_path.query))
            }.get(parsed_path.path, self.do_no())
        }
        

        self._set_headers()
        self.wfile.write(bytes(json.dumps(response), "utf-8"))
        '''
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        '''

    def do_aaa(self, args):
        return 'aaa'

    def do_bbb(self, args):
        return 'bbb'

    def do_no(self):
        return '404'

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))