import logging
import multiprocessing
 
from multiprocessing import Process, Lock
 
 
lock = Lock()
 
 
def square(num,i):
    """
    Prints out the item that was passed in
    """
    l=multiprocessing.Array('i',10)
    lock.acquire()
    try:
       l[i]=num*num 
       
    finally:
        lock.release()
        
    
if __name__ == '__main__':
    nos = [i+1 for i in range(10)]
    for no in range(len(nos)):
        p = Process(target=square, args=(nos[no],no))
        p.start()
