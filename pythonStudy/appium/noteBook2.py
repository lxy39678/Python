'''
搜索
输入小米
点击股票类型
点击小米股票
'''
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class ContactsAndroidTests(unittest.TestCase):
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

        # self.driver.find_element_by_id("com.xueqiu.android:id/open").click()
        # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        print(self.driver.page_source)
        self.driver.get_screenshot_as_file("start.png")
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("xiaomi")
        self.driver.find_element_by_xpath("//*[@text='股票' and @resource-id='com.xueqiu.android:id/text']").click()
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@instance=13]").click()
        self.driver.implicitly_wait(5)
        self.driver.quit()

    def test_swipe(self):
        sleep(5)
        TouchAction(self.driver).press(x=800, y=1000).move_to(x=150, y=1000).release().perform()
        TouchAction(self.driver).press(x=600, y=1500).move_to(x=600, y=1000).release().perform()




if __name__ == '__main__':
    unittest.main()