
class UrlsPool:

    def __init__(self, base_url_1, initial_num, n, base_url_2=''):
        self.base_url_1 = base_url_1
        self.initial_num = initial_num
        self.n = n
        self.base_url_2 = base_url_2
        self.urlspool = set()

    def create(self):
        for i in range(1, self.n+1):
            self.urlspool.add(self.base_url_1 + str(self.initial_num+i) + self.base_url_2)
        return self.urlspool

    def remove(self, crawled_url):
        self.urlspool.remove(crawled_url)
