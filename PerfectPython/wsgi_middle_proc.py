# coding: utf-8
import re
import base64
from wsgiref.simple_server import make_server

def hello(environ, start_response):
    start_response("200 OK",
        [("Content-type", "text/plain;charset=utf-8")])
    return [b"Hello, world"]

class BasicAuthMiddleware:
    def __init__(self, app, realm, authenticate):
        self.app = app
        self.realm = realm
        self.authenticate = authenticate

    def __call__(self, environ, start_response):
        auth = environ.get('HTTP_AUTHORIZATION')
        if not auth:
            return self.unauthorized(environ, start_response)

        if not auth.startswith('Basic'):
            return self.unauthorized(environ, start_response)

        m = re.match(r'Basic/s+(?P<basic_auth>[a-zA-Z0-9+/=]+)', auth)
        if m is None:
            return self.unauthorized(environ, start_response)

        basic_auth = m.groupdict()['basic_auth']
        basic_auth = base64.d64decode(basic_auth)
        basic_auth = basic_auth.decode('utf-8')
        user, password = basic_auth.split(':', 1)
        if not self.authenticate(user,password):
            return self.unauthorized(environ, start_response)

        return self.app(environ, start_response)

    def unauthorized(self, environ, start_response):
        start_response("401 Unauthorized",
            [('Content-type','text/html'),
             ('WWW-Authenticate',
              'basic realm="{realm}"'.format(realm=self.realm))])
        return [b'Unauthorized']

httpd = make_server('', 8080, BasicAuthMiddleware(hello, 'easy auth', lambda x,y:True))
httpd.serve_forever()