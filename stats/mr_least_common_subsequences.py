# yield the 100 subsequences that appear in the most passwords
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from queue import PriorityQueue

class MRCommonSubsequences(MRJob):

  INPUT_PROTOCOL = JSONValueProtocol

  def mapper(self, _, dictionary):
      '''
      reads in json objects from the output file and digs into the
      list of lists in the 'pattern' key to yield the subsequence
      along with a count of -1. I use the count of -1 in order to be 
      able to use the Priority Queue structure which is ideal to find
      the top N most frequent objects, to find the top N LEAST frequent objects.
		  '''
      #{"password": "14081408", "pattern": [["140", "numbers"], ["814", "date"], ["08", "numbers"]]}
      for pattern_list in dictionary['pattern']:
          yield pattern_list[0],-1

  def combiner(self, name, counts):
      sum_counts = sum(counts)
      yield name, sum_counts

  def reducer_init(self):
     '''
     generates a priority queue to track the top 100
     '''
    
     self.queue = PriorityQueue(maxsize=100)

  def reducer(self, name, counts):
      sum_counts = sum(counts)
      if not self.queue.full():
        self.queue.put(tuple([sum_counts,name]))

      else:
        min_top = self.queue.get()
        if sum_counts > min_top[0]:
            self.queue.put(tuple([sum_counts,name]))
        else:
            self.queue.put(min_top)


  def reducer_final(self):
      while not self.queue.empty():
          yield self.queue.get()

if __name__ == '__main__':
  MRCommonSubsequences.run()
