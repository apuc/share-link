import mimetypes
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from urllib.parse import parse_qs


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        type = mimetypes.guess_type('../123.jpg')
        self.send_header('Content-type', type[0])
        self.end_headers()

        parsed = urlparse.urlparse(self.path)
        params = parse_qs(parsed.query)
        if params.get('file'):
            print(type)
            print(params.get('file'))

        f = open('123.jpg', "rb")
        self.wfile.write(f.read())
        f.close()

        return