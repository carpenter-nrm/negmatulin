from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()
    
server = HTTPServer(('localhost', 6789) , MyHandler )
print('Site is active: http://localhost:6789')
server.serve_forever()