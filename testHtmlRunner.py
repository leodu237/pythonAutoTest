# -*- coding:utf-8 -*-
import unittest
import unittest001
import HTMLTestRunner

#构造测试集
suit = unittest.TestSuite()

suit.addTest(unittest001.TestOne("test_add"))
suit.addTest(unittest001.TestOne("test_sub"))

if __name__ == "__main__":
	'''不使用HTMLTestRunner的方式执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''

	#定义报告存放路径
	fp = open('/Users/dulongnian/PycharmProjects/XJYStudy/result.html','wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title= u'测试-测试报告',description='用例执行情况：')
	runner.run(suit)
	fp.close