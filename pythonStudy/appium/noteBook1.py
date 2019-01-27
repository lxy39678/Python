'''
主页面的个人信息图标
登录雪球
手机及其他登录
邮箱手机号登录
输入用户名密码
'''

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/open")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el4.click()
sleep(5)
el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_with_account")
el7.click()
el8 = driver.find_element_by_id("com.xueqiu.android:id/login_account")
el8.send_keys("1000000000")
el9 = driver.find_element_by_id("com.xueqiu.android:id/login_password")
el9.send_keys("111111111")

driver.quit()