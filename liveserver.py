from livereload import Server

def serve(app):
    server = Server(app.wsgi_app)
    server.serve()