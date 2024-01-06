import time
import multiprocessing
import concurrent.futures
start = time.perf_counter()

def foo(n):
    print(f'Running...{n}')
    time.sleep(n)
    return'End of the task'

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as ex:
        seconds = [5,4,3,2,1]
        result = ex.map(foo,seconds)


        for i in result:
            print(i)

#     for _ in range(1,100):
#         res = []
#
#         for _ in range(1, 100):
#             p = multiprocessing.Process(target=foo,args=[_])
#             p.start()
#             res.append(p)
#
#         for p in res:
#             p.join()
#
# finish = time.perf_counter()
#
# print(f'Result time {round(finish-start,2)}')