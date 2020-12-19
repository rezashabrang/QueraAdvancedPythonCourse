from threading import Thread
from functions import f
from functions import g
from functions import h
def solve():
    t1 = Thread(name='1', target=f[0])
    t2 = Thread(name='2', target=f[1])
    t3 = Thread(name='3', target=f[2])
    t4 = Thread(name='4', target=f[3])
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5 = Thread(name='1', target=g[0])
    t6 = Thread(name='2', target=g[1])
    t5.start()
    t6.start()
    t5.join()
    t6.join()
    t7 = Thread(name='1',target=h[0])
    t7.start()
    t7.join()

