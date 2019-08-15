from selenium import webdriver


class Spider:

    def __init__(self, spider_name, url_part_1, initial_num, iterator, url_part_2=''):
        self.spider_name = spider_name
        self.url_key = initial_num + iterator
        self.url = url_part_1 + str(self.url_key) + url_part_2
        self.crawl()

    def crawl(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        print(self.spider_name, 'now crawling', self.url_key)

        self.project_name = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[1]/td[2]')
        self.project_number = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[2]/td[2]')
        self.project_intro = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[3]/td[2]')
        self.project_link = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[4]/td[2]')
        self.project_purpose = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[5]/td[2]')
        self.project_size = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[6]/td[2]')
        self.project_duration = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[7]/td[2]')
        self.project_apr = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[8]/td[2]')
        self.project_repay_start = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[9]/td[2]')
        self.project_repay_method = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[10]/td[2]')
        self.project_repay_details = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[11]/td[2]')
        self.project_status = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[12]/td[2]')
        self.project_raise_start = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[13]/td[2]')
        self.project_guarantee = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[14]/td[2]')
        self.project_repay_source = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[15]/td[2]')
        self.project_risk = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[16]/td[2]')
        self.project_expense = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[17]/td[2]')
        self.project_template_number = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[18]/td[2]')
        self.project_lender_notice = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[19]/td[2]')
        self.project_borrower_type = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[20]/td[2]')

        self.list_of_attribute = [self.url_key, self.project_name.text, self.project_number.text, self.project_intro.text, self.project_link.text, self.project_purpose.text, self.project_size.text,
                                  self.project_duration.text, self.project_apr.text, self.project_repay_start.text, self.project_repay_method.text, self.project_repay_details.text,
                                  self.project_status.text, self.project_raise_start.text, self.project_guarantee.text, self.project_repay_source.text, self.project_risk.text,
                                  self.project_expense.text, self.project_template_number.text, self.project_lender_notice.text, self.project_borrower_type.text]

        driver.close()
        print(self.spider_name, 'has finished the crawling from', self.url_key)

    def get_list(self):
        return self.list_of_attribute
