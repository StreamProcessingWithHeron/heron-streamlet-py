from random import choice
from time import sleep

from heronpy.streamlet.generator import Generator 

class SlowGenerator(Generator): 
  def setup(self, context): 
    self._words = (
      'nathan', 'mike', 'jackson', 'golda', 'bertels')

class SlowGenerator1(SlowGenerator):
  def get(self):
    sleep(1) 
    return choice(self._words) 

class SlowGenerator2(SlowGenerator):
  def get(self):
    sleep(1.5)
    return (choice(self._words), choice(self._words)) 
    
from heronpy.streamlet.builder import Builder
from heronpy.streamlet.config import Config
from heronpy.streamlet.runner import Runner

if __name__ == '__main__':
  builder = Builder() 

  stream_1 = builder.new_source(SlowGenerator1()) 
  stream_2 = builder.new_source(SlowGenerator2()) 

  stream_3 = stream_1.map(lambda x: x + " !!!") 
  stream_4 = stream_2 \
    .map(lambda x: x[0] + " & " + x[1] + " !!!") 

  stream_3.union(stream_4).map(lambda x: x + " !!!").log() 

  Runner().run("my-python-streamlet", Config(), builder) 