import unittest
from models import sources


Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    
    def setUP(self):
        self.new_sources = Sources('bbc-news','name','description','url','urlToImage','title','publish','none','jupiter')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))
        
if __name__=='__main__':
    unittest.main()
       
        