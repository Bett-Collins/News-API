import unittest
from models import sources


Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    
    def setUP(self):
        self.new_sources = Sources('abc-news','ABC News,Your trusted source for breaking news, analysis', 'exclusive interviews', 'headlines, and videos at ABCNews.com','https://abcnews.go.com','us')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))
        
if __name__=='__main__':
    unittest.main()
       
        