#Import flask
from flask import Flask;
from app import app;

@app.route('/')
def hello():
    """Renders a sample page."""
    return """<html> 
                   <head>
                        <title>
                           Hello World
                        </title>
                   </head>
                   <body>
                        <h1>Hello World Shohag</h1>
                   <body>        
             </html>"""
    

@app.route("/create")
def create():
    return """<html> 
                   <head>
                        <title>
                           Create Page
                        </title>
                   </head>
                   <body>
                        <h1>Write Your Create Form here...</h1>
                   <body>        
             </html>"""
