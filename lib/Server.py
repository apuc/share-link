from http.server import BaseHTTPRequestHandler, HTTPServer
from lib.Handler import Handler


class Server:

    def create_server(self, host, port):
        server = HTTPServer((host, port), Handler)
        server.serve_forever()