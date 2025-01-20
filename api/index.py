from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        url = self.path
        parsed = parse_qs(urlparse(url).query)

        with open('q-vercel-python.json', 'r') as f:
            input_json = f.read() 
            # Transform json input to python objects
            input_dict = json.loads(input_json)
            self.wfile.write(str(input_dict).encode('utf-8'))
            # Filter python objects with list comprehensions
            output_dict = [x for x in input_dict if x['name'].isin(parsed)]
            
            # Transform python object back into json
            output_json = json.dumps(output_dict)
            self.wfile.write(str(output_json).encode('utf-8'))
        return
