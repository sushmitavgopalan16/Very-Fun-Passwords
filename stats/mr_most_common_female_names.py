# yield the 100 most common female names
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from queue import PriorityQueue

class MRFemaleNames(MRJob):

  INPUT_PROTOCOL = JSONValueProtocol

  def mapper(self, _, dictionary):
        for pattern_list in dictionary['pattern']:
            if  pattern_list[1] == "female name":
                yield pattern_list[0],1

  def combiner(self, name, counts):
      sum_counts = sum(counts)
      yield name, sum_counts

  def reducer_init(self):
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
  MRFemaleNames.run()
