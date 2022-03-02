import unittest
from models import news

News = news.News


class NewsTest(unittest.TestCase):


    def setUp(self):

        self.new_news = News('bbc-news','name','description','url','urlToImage','title','publish','none')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


if __name__ == '__main__':
    unittest.main()