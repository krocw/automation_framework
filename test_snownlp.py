# _*_ coding=utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.home_page import HomePage


class TestSnowNLP(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:

        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_snowNLP(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """

        homepage = HomePage(self.driver)
        homepage.send_textarea('你真漂亮')  # 调用页面对象中的方法
        homepage.send_begin_btn()  # 调用页面对象类中的点击按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        result = self.driver.find_element_by_class_name("animated")
        print(result)
        try:
            assert result.text == '4.506021100858332'
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))
