from http.server import SimpleHTTPRequestHandler, HTTPServer

HTTPServer(('', 8000), SimpleHTTPRequestHandler).serve_forever()
