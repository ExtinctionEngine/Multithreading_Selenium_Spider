from housekeeping import *
import threading
from queue import Queue
import spider


PROJECT_NAME = 'renrendai'
PROJECT_URL_1 = 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=911101055548793445'
PROJECT_INITIAL_NUM = 2668603
PROJECT_MAX_PAGES = 1000000
PROJECT_URL_2 = '&sdebtortypeb=01&sfullnames=911101055548793445'
NUMBER_OF_SPIDERS = 12
queue = Queue()

create_data_csv(PROJECT_NAME)
create_iterator_set(PROJECT_MAX_PAGES)


def create_spiders():
    for _ in range(NUMBER_OF_SPIDERS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get() # when get() is proceed, it blocks and waits until queue has something to return
        spider.Spider(thread_name, url)
        queue.task_done()

def create_jobs():
    for link in

