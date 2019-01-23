from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from sys import getfilesystemencoding
from re import compile


url_regex = compile(r'(?P<resource>[^?#]*)(\?(?P<querystring>[^#]*))?(\#(?P<fragment>.*))?')
url_fields = 'resource', 'querystring'
fs_encoding = getfilesystemencoding()

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        headers = self.headers

        m = url_regex.match(self.path)
        thead = '<td><h2>field</h2></td><td></td><td><h2><i>value</i><h2></td>'
        tbody = ''.join('<tr><td><b>%s</b></td><td></td><td><i>%s</i></td></tr>' % (f, m.group(f)) for f in url_fields)
        table = '<table><thead>%s</thead><tbody>%s</tbody></table>' % (thead, tbody)
        content = table.encode()

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html; charset=%s' % fs_encoding)
        self.send_header('Content-Length', str(len(content)))
        self.send_header('Set-Cookie', 'foo=bar')
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        path = self.path
        headers = self.headers

        content_length = self.headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        content = self.rfile.read(length)

        self.send_response(HTTPStatus.OK)

    do_PUT = do_POST
    do_DELETE = do_GET


def run(addr='0.0.0.0', port=8000):
    print('Listening on http://%s:%d' % (addr, port))
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    run()
