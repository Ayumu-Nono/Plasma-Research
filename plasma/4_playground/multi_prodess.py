from multiprocessing import Pool
from tqdm import tqdm
import time


def f(x):
    for x in tqdm(range(100000000)):
        x = x* x
    return x*x

if __name__ == '__main__':
    start = time.time()
    pool_num = 10
    with Pool(pool_num) as p:
        print(p.map(f, [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6,
        1, 2, 3, 4, 5, 6]))
    elapsed_time = time.time() - start
    print('pool number ', pool_num)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")