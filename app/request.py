from inspect import getsource
from app import app
import urllib.request,json

from .models import sources

Sources = sources.Sources
news_api = 'https://newsapi.org/v2/top-headlines/sources?apiKey=d2058fcf62674d56874e601e24678c59'


def get_sources(sources):
    with urllib.request.urlopen(news_api) as url:
        get_source_data = url.read()
        source_response = json.loads(get_source_data)
        
        source_results = None
        
        if source_response['sources']:
            
            news_sources_list = source_response['sources']
            source_results = load_results(news_sources_list)
            
    return source_results

def load_results(sources_list):
    source_results = []
    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        description =item.get('description')
        url = item.get('url')
        country =item.get('country')
        
        if name:
            source_object = Sources(id,name,description,url,country)
            source_results.append(source_object)
            

            
    return source_results
        
    
                
            
        
            
        