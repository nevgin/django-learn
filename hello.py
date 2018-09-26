def wsgi_application(environ, start_response):
    status="200 OK"
    body="Hello World"
    headers=[("Content-Type", "text/plain"),("Content-Length",str(len(body)))]
    start_response(status,headers)
    return [body]


