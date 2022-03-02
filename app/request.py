from app import app
import urllib.request, json
from . models import news

News = news.News



NEWS_TOP ='https://newsapi.org/v2/top-headlines?country=us&apiKey=d2058fcf62674d56874e601e24678c59'


def get_news(articles):

    

    with urllib.request.urlopen(NEWS_TOP) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)


        news_results = None

        if get_news_response['articles']:

            news_results_list = get_news_response['articles']

            news_results = process_results(news_results_list)


        
    return news_results




def process_results(news_list):

    news_results = []
    for news_item in news_list:
        source_name = news_item.get('source_name') 
        author = news_item.get('author')
        description =news_item.get('description')
        url =news_item.get('url')
        title = news_item.get('title')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
     

    if source_name:

            news_object = News(source_name,author,description,url,title,urlToImage,publishedAt,content)
            news_results.append(news_object)



    return news_results







     