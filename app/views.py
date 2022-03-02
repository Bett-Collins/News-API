

from flask import render_template
from app import app
from . request import get_sources

from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():


    header="Welcome to the best news application online"
    title= "Home - Welcome to the best news application online"
    top_news = get_news('articles')
    print(top_news)
    
    
   
    



    return render_template('index.html', title=title, header=header, articles =top_news)
    
    
