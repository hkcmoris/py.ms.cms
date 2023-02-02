from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import webbrowser


class RequestHandler(BaseHTTPRequestHandler):

    def loadApi(self, api):
        self.api = api

    def do_GET(self):
        sendReply = False
        params = self.path.split('?')
        if len(params) > 1:
            self.path = params[0]
            params = params[1].split('&').forEach(
                lambda x: x.split('='))
        if self.path == '/':
            self.path = '/index.html'
            sendReply = True
        if self.path.endswith('.html'):
            mimetype = 'text/html'
            sendReply = True
        if self.path.endswith('.css'):
            mimetype = 'text/css'
            sendReply = True
        if self.path.endswith('.js'):
            mimetype = 'application/javascript'
            sendReply = True
        if self.path.endswith('.png'):
            mimetype = 'image/png'
            sendReply = True
        if self.path.endswith('.jpg'):
            mimetype = 'image/jpg'
            sendReply = True
        if self.path.endswith('.jpeg'):
            mimetype = 'image/jpeg'
            sendReply = True

        if sendReply:
            try:
                with open(os.path.join('www', self.path[1:]), 'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    content = f.read()
                    with open(os.path.join('server', 'config.json'), 'rb') as k:
                        keywords = json.load(k)
                        for keyword in keywords:
                            if keyword.encode() in content:
                                content = content.replace(
                                    keyword.encode(), self.do_APIRequest(keyword).encode())
                    self.wfile.write(content.replace(
                        b"<!--#title-->", self.path[1:].encode()))
                return
            except IOError:
                self.send_response(404)
                pass

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.do_APIRequest('Hello World!').encode())

    def do_APIRequest(self, request):
        if self.api == None:
            return None

        match request:
            case "welcome_page":
                return self.api.welcomePage()
            case _:
                return self.api.request(request)


class httpserver:

    def __init__(self, port, api):
        self.server_address = ("", port)
        self.httpd = HTTPServer(self.server_address, RequestHandler)
        self.httpd.RequestHandlerClass.loadApi(
            self.httpd.RequestHandlerClass, api)

    def start(self):
        print(f"Starting web server on port {self.server_address[1]}")
        print(
            f"Open http://localhost:{self.server_address[1]} in your browser")
        webbrowser.open(f"http://localhost:{self.server_address[1]}")
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()
