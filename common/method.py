def open(driver,url):
    driver.get(url)

import time
def login(driver,username,password):
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

def search(driver,url, username, password,key):
    open(driver,url)
    login(driver, username, password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    id2 = id + '-frame'
    driver.switch_to.frame(id2)
    driver.find_element_by_id('searchNumber').send_keys(key)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(2)
    n = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
    return n
