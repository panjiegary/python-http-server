"""Create a http server."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyRequestHandler(BaseHTTPRequestHandler):
    """Handle request."""

    def do_GET(self):
        """Handle get request."""
        if self.path == "/hello":
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('hello.html', 'rb') as fp:
                self.wfile.write(fp.read())
        else:
            self.send_response(404)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        return


def run():
    """Start server."""
    print('starting server...')
    server_address = ('127.0.0.1', 8888)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
