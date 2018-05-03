# _*_ coding = utf-8 _*_
import unittest
from tools import HTMLTestRunner
import os
from testsuites.test_snownlp import TestSnowNLP
from testsuites.test_douban import TestDouBan
from testsuites.test_canting import TestCanTing
import time

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

suite = unittest.TestSuite()
suite.addTest(TestSnowNLP('test_snowNLP'))
suite.addTest(TestDouBan('test_douban'))
suite.addTest(TestCanTing('test_canting'))

if __name__ == '__main__':
    # 执行用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"中文短文本情感分析测试报告", description=u"用例测试情况")
    runner.run(suite)
