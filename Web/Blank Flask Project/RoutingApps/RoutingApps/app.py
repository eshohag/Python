"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


#@app.route('/')
#def hello():
#    """Renders a sample page."""
#    return """<html> 
#                   <head>
#                        <title>
#                           Hello World
#                        </title>
#                   </head>
#                   <body>
#                        <h1>Hello World Shohag</h1>
#                   <body>        
#             </html>"""
    

#@app.route("/create")
#def create():
#    return """<html> 
#                   <head>
#                        <title>
#                           Create Page
#                        </title>
#                   </head>
#                   <body>
#                        <h1>Write Your Create Form here...</h1>
#                   <body>        
#             </html>"""

#Access the routes file from RoutingFile/routes.py

from routes import *;



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
