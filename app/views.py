#!/usr/bin/python
#
from app import app

@app.route('/')

@app.route('/index')

def index():
    user = {'nicename':'zhangyang'}
    return '''
<html>
  <head>
    <title> Home page </title>
  </head>
  <body>
    <h1> hello, %s </h1>
  </body>
</html> ''' % (user['nicename'])


