import random
import time
from threading import Thread
'''
Muratcan Erek
180316042
'''
class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1

class CalculateEuler:

    def __init__(self):
        self.count = 0 #Total of works
        self.total = 0 #Total number at random intervals

    def Euler(self, n):

        random_number = 0
        count_random = 0
        for i in range(n):
            while random_number <= 1:
                b = round(random.random(), 5) #degree of precesion is 5 you can change.but (!=1)
                random_number += b
                count_random += 1
            self.total += count_random
            random_number = 0
            count_random = 0
            self.count += 1


if __name__ == "__main__":

    n = 1000000
    tictoc = TicToc()
    tictoc.tic()
    find_eu = []
    threads = []
    amount_thread = 8
    for i in range(amount_thread):
        find_eu.append(CalculateEuler())
        threads.append(Thread(target=find_eu[i].Euler, args=(n,)))
        print("Started thread number #%d" % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    total = 0
    count = 0
    for findeu in find_eu:
        total += findeu.total
        count += findeu.count
    print("Euler Number: %.5f | N: %d | Time: %.3f" % ((total/count), count, tictoc.toc()))


