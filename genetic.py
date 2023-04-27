import numpy as np
import Gene

class GeneticAlgorithm():
  def __init__(self, gene_list):
      self.genes = gene_list[:]

  # evaluate the genes need to be reproduce / where to put??  
  def fitness(self):
      pass

  # make match pool
  def reproduction(self):
      pass

  # crossover in the match pool
  def crossover(self):
      pass

  # add some noise
  def mutation(self):
      pass


# temporary
if __name__ == '__main__':
    print("start")