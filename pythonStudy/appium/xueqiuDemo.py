import unittest
from time import sleep
from appium import webdriver


caps = {}
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps ["platformName"] = "android"
caps["deviceName"] = "ddd"

driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
driver.implicitly_wait(5)

# el1 = driver.find_element_by_id("//*[@text='自选' and @resource-id='com.xueqiu.android:id/tab_name']")
el1 = driver.find_element_by_id("com.xueqiu.android:id/agree")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
driver.find_element_by_id("stockName").click()
driver.quit()