import time
from tqdm import tqdm


if __name__ == '__main__':
    start = time.time()
    for i in tqdm(range(100000000)):
        pass
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")