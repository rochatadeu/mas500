import mediacloud
from API_config import MY_API_KEY

class Sentences_september:

   def __init__(self, word):
      self.word = word
      self.mc = mediacloud.api.MediaCloud(MY_API_KEY)
   
   def fetch(self):
      self.sentencecount = self.mc.sentenceCount(self.word, '+publish_date:[2016-09-01T00:00:00Z TO 2016-10-01T00:00:00Z} AND +tags_id_media:1')
        
   def result(self):
      return self.sentencecount['count']


      