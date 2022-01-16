import threading
from queue import Queue
from gen import *
from domain_name import *
from spider import Spider

#
# PROJECT_NAME = 'viper-seo'
# HOMEPAGE = 'http://viper-seo.com/'

# PROJECT_NAME = 'thenewboston'
# HOMEPAGE = 'https://thenewboston.com/'

PROJECT_NAME = 'geeks'
HOMEPAGE = 'https://www.geeksforgeeks.org/'

DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_workers():
    """
    create worker threads
    :return: None
    """
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    """
    do the next job in queue
    :return: None
    """
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_jobs():
    """
     each queued link is a job
    :return: None
    """
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    """
    check if there are items in the queue if so crawl
    :return: None
    """
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


if __name__ == '__main__':
    create_workers()
    crawl()
