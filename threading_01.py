import time
import threading

start = time.perf_counter()


def index():
    print('Starting...')
    time.sleep(5)
    print('end of the fun')

threads = []
for _ in range(1,10):
    t = threading.Thread(target=index)
    t.start()
    threads.append(t)


thread_1 = threading.Thread(target=index)
thread_2 = threading.Thread(target=index)


thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'End {round(finish - start)}')
