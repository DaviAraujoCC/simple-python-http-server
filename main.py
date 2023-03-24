#!/bin/env python3

import http.server
import socketserver

PORT = 8080

class HelloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, World!')
            return
        else:
            
            self.send_error(404)

with socketserver.TCPServer(("", PORT), HelloHandler) as httpd:
    print("Server listening on port", PORT)
    httpd.serve_forever()