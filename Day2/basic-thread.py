'''
module basic thread

A very basic thread example
'''
from time import sleep
import threading

def print_numbers(name, start =1, end=10, skip=1):
    for i in range(start, end+1, skip):
        print ('in thread {} value of i is {}'.format(name, i))
        sleep(0.5)

def main():
    print ('main started')
    t1 = threading.Thread(target=print_numbers, args=('first',))
    t2 = threading.Thread(target=print_numbers, args=('second',))
    t1.start() # Does not call the run() of the thread class
    t2.start() # # Does not call the run() of the thread class
    t1.join()
    t2.join()
    print ('main ended')

if __name__ == "__main__":
    main()