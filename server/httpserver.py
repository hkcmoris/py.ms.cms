from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello World!')

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello World!')


class httpserver:

    def __init__(self, port):
        self.server_address = ("", port)
        self.httpd = HTTPServer(self.server_address, RequestHandler)

    def start(self):
        print(f"Starting web server on port {self.server_address[1]}")
        print(
            f"Open http://localhost:{self.server_address[1]} in your browser")
        webbrowser.open(f"http://localhost:{self.server_address[1]}")
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()
