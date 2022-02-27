from inspect import getsource
from app import app
import urllib.request,json

from .models import sources

Sources = sources.Sources

# #Getting api key

# new_api = app.config[' API_KEY ']

# #Getting the base url

# base_url = app.config['base_Url']

news_api = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d2058fcf62674d56874e601e24678c59'


def get_sources(articles):
    with urllib.request.urlopen(news_api) as url:
        get_source_data = url.read()
        source_response = json.loads(get_source_data)
        
        source_results = None
        
        if source_response['articles']:
            
            news_sources_list = source_response['articles']
            source_results = load_results(news_sources_list)
            
    return source_results

def load_results(sources_list):
    source_results = []
    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        author = item.get('author')
        description =item.get('description')
        url =item.get('url')
        title = item.get('title')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        content = item.get('content')
       
        if name:
            source_object = Sources(id,name,author,description,url,title,urlToImage,publishedAt,content)
            source_results.append(source_object)
            

            
    return source_results
        
    
                
            
        
            
        