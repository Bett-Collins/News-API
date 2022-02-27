

from flask import render_template
from app import app
from . request import get_sources

@app.route('/')
def index():
    
    message = 'Python application'
    
    sources = get_sources('articles')
    print(sources)
    
    
    return render_template('index.html',sources = sources, message = message)  

