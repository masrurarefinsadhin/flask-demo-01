from app import app
from flask import render_template
@app.route('/')
def index():
    user = {'userName': 'Noob'}
    return '''
    <html>
        <head></head>
        <body>
            <h1> Hey ''' +user['userName']+''' </h1>  
        </body>
    </html>'''

@app.route('/index')
def indexTemplate():
    user = {'userName', 'default'}
    posts=[ 'to br or not to be - YODA', 'say the magic word -Eminem']
    return render_template('index.html', user=user, posts=posts)