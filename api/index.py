from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        url = self.path
        parsed = parse_qs(urlparse(url).query)

        with open('q-vercel-python.json', 'r') as f:
            for line in f:
                self.wfile.write(str(parsed).encode('utf-8'))
        return
