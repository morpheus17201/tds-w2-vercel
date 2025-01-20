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
        input_data = json.loads(input_json)
      
        output_list = []
        for name in parsed['name']:
            for ele in input_data:
                if ele['name'] == name:
                    output_list.append(str(ele['marks']))
 

        output_json = '{ "marks": [' +', '.join(output_list) + "] }"
        self.wfile.write(str(output_json).encode('utf-8'))
        return
