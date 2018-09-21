





def login(driver):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("yuanjunling")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("1234")
    driver.find_element_by_id("captcha").clear()
    driver.find_element_by_id("captcha").send_keys("greattao0818")
    driver.find_element_by_xpath(".//*[@id='fm1']/section[5]/input[4]").click()


