from selenium import webdriver
import random
from housekeeping import *
from urlpool import *


class Spider:

    # Class variables shared among all instances
    baseurl_1 = ''
    baseurl_2 = ''

    def __init__(self, project_name, baseurl_1, initial_num, i, baseurl_2):
        self.project_name = project_name
        self.urls = UrlsPool(baseurl_1, initial_num, i, baseurl_2)
        self.url = random.choice(self.urls)
        self.list_of_attributes = list()
        self.crawl()
        self.upade_set()

    def crawl(self):

        driver = webdriver.Chrome()
        driver.get(self.url)

        project_name = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[1]/td[2]')
        project_number = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[2]/td[2]')
        project_intro = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[3]/td[2]')
        project_link = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[4]/td[2]')
        project_purpose = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[5]/td[2]')
        project_size = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[6]/td[2]')
        project_duration = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[7]/td[2]')
        project_APR = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[8]/td[2]')
        project_repay_start = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[9]/td[2]')
        project_repay_method = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[10]/td[2]')
        project_repay_details = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[11]/td[2]')
        project_status = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[12]/td[2]')
        project_raise_start = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[13]/td[2]')
        project_guarantee = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[14]/td[2]')
        project_repay_source = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[15]/td[2]')
        project_risk = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[16]/td[2]')
        project_expense = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[17]/td[2]')
        project_template_number = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[18]/td[2]')
        project_lender_notice = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[19]/td[2]')
        project_borrower_type = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[20]/td[2]')

        self.list_of_attributes = [project_name.text, project_number.text, project_intro.text, project_link.text, project_purpose.text, project_size.text,
                                   project_duration.text, project_APR.text, project_repay_start.text, project_repay_method.text, project_repay_details.text,
                                   project_status.text, project_raise_start.text, project_guarantee.text, project_repay_source, project_risk.text,
                                   project_expense.text, project_template_number.text, project_lender_notice.text, project_borrower_type.text]

        return self.list_of_attributes

    def upade_set(self):
        self.urls.remove(self.url)
        return self.urls











