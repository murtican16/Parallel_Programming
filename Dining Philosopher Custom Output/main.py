import random
import time
from threading import Thread, Lock


class DiningPhilosophers:
    def __init__(self, number_of_philosopher, meal_size):
        self.meals = [meal_size for _ in range(number_of_philosopher)]
        self.chopsticks = [Lock() for _ in range(number_of_philosopher)]
        self.status = ['T' for _ in range(number_of_philosopher)]
        self.keepR = [' ' for _ in range(number_of_philosopher)]
        self.keepL = [' ' for _ in range(number_of_philosopher)]
        self.countchop = [0 for _ in range(number_of_philosopher)]



    def philosopher(self, i):
        while self.meals[i] > 0:
            self.status[i] = 'T'
            j = (i+1) % 5
            '''print("Philosopher %d is thinking" % i)'''
            time.sleep(random.random())
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                self.keepR[i] = '-'
                self.countchop[i] += 1
                '''print("Philosopher %d has the chopstick %d" % (i, i))'''
                time.sleep(random.random())
                if self.chopsticks[j].locked():
                    self.chopsticks[i].release()
                    self.keepR[i] = ' '
                    self.countchop[i] -= 1

                    '''print("The chopstick %d is locked, so chopstick %d is released" % (j, i))'''
                else:
                    self.chopsticks[j].acquire()
                    self.keepL[i] = '-'
                    self.countchop[i] += 1

                    '''print("Philosopher %d has the chopsticks %d and %d" % (i, i, j))'''
                    '''print("Philosopher %d is eating" % i)'''
                    self.status[i] = 'E'
                    self.meals[i] -= 1
                    time.sleep(random.random())
                    self.chopsticks[j].release()
                    self.keepL[i] = ' '
                    self.countchop[i] -= 1

                    '''print("Philosopher %d released chopstick %d" % (i, j))'''
                    self.chopsticks[i].release()
                    '''print("Philosopher %d released chopstick %d" % (i, i))'''
                    self.status[i] = 'T'
                    self.keepL[i] = ' '
                    self.keepR[i] = ' '
                    self.countchop[i] = 0



def main():
    n = 5
    m = 10
    chopstick_count = 0
    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()

    while sum(dining_philosophers.meals) > 0:
        print("        "+dining_philosophers.keepL[0]+dining_philosophers.status[0]+dining_philosophers.keepR[0]+"\n\n" +

              "   "+dining_philosophers.keepL[4] + dining_philosophers.status[4]+dining_philosophers.keepR[4]+"       "
              + dining_philosophers.keepL[1]+dining_philosophers.status[1]+dining_philosophers.keepR[1]+"\n\n"+

              "     "+dining_philosophers.keepL[3]+dining_philosophers.status[3]+dining_philosophers.keepR[3]+"   " +
              dining_philosophers.keepL[2]+dining_philosophers.status[2]+dining_philosophers.keepR[2]+"\n\n")

        chopstick_count = sum(dining_philosophers.countchop)
        print("Number of eating philosophers: %d / 5" % (dining_philosophers.status.count('E')))
        print("Number of locked chopsticks: %d / 5" % chopstick_count)
        print("Meals left: %d / %d" % (sum(dining_philosophers.meals), m*n))
        """ print(dining_philosophers.countchop)"""
        print("\n\n")
        time.sleep(0.3)

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()


