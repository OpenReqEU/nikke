# Import your application as:
# from app import application
# Example:

from code import app

# Import CherryPy
import cherrypy

if __name__ == '__main__':

    # Mount the application
    cherrypy.tree.graft(app, "/")

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    cherrypy.config.update('server.cfg')

    # Configure the server object
    server.socket_host = cherrypy.config.get("server.socket_host")
    server.socket_port = 9209
    server.thread_pool = 30
    server.socket_timeout = 300
    server.max_request_body_size = 0

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    server.subscribe()

    # Start the server engine (Option 1 *and* 2)

    cherrypy.engine.start()
    cherrypy.engine.block()
