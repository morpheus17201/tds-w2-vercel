from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        with open('q-vercel-python.json', 'r') as f:
            for line in f:
                self.wfile.write(line.encode('utf-8'))
        return
