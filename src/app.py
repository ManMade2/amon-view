from amon_view import create_app
from livereload import Server


app = create_app()
app.config['TEMPLATES_AUTO_RELOAD'] = True


if __name__ == '__main__':
    
    server = Server(app.wsgi_app)

    server.watch('src/amon_view/static/dist/')
    server.watch('src/amon_view/templates/')
    server.watch('*.py')  # Watch Python files too

    # Start the server
    server.serve(port=5000, debug=True, restart_delay=10)