'''
行情
板块
银行
滚动到最后
选择最后一个股票
'''
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class ContactsAndroidTests1(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyBoard"] = "true"
        caps["resetKeyboard"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@instance=19]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='板块' and @resource-id='com.xueqiu.android:id/text']").click()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@instance=15]").click()
        TouchAction(self.driver).press(x=500, y=1700).move_to(x=500, y=300).release().perform()
        TouchAction(self.driver).press(x=500, y=1700).move_to(x=500, y=300).release().perform()
        TouchAction(self.driver).press(x=500, y=1700).move_to(x=500, y=300).release().perform()
        TouchAction(self.driver).press(x=500, y=1700).move_to(x=500, y=300).release().perform()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[@instance=27]").click()
        self.driver.implicitly_wait(15)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()