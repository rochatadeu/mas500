from hw2_fetch import Sentences_september
import unittest

class SentencesSeptTest(unittest.TestCase):

    def setUp(self):
        self.results = Sentences_september('Trump')

    def testFetch(self):
        self.results.fetch()
        assert self.results is not None
        
    def testResult(self):     
        self.results.fetch()
        self.sentence_count = self.results.result()
        assert self.sentence_count > 0

# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()