#coding=utf-8
import sys
sys.path.append('D:\\JT_selenium')
import traceback
from unittest import TestSuite
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import unittest
import os
import time
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = "D:/JT_selenium/Image/test.png"
        cls.file_name2 = "D:/JT_selenium/Image/test2.png"
        cls.driver = webdriver.Chrome()
        cls.driver.get('**********************************')
        cls.driver.maximize_window()
    def setUp(self):
        self.logger.info("this is chrome")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()

    #正常登录
    def test_login_success(self):
        success = self.login.user_base('JTZF800008','ali@163.com','123123',self.file_name)

    #修改密码
    def test_login_changepasword(self):
        changepasword = self.login.user_base2('111111','111111',self.file_name)

    #修改支付密码
    def test_login_changepaypasword(self):
        changepaypasword = self.login.user_base3('222222','222222',self.file_name)

    #绑定谷歌验证码
    def test_login_bindingcode(self):
        bindingcode = self.login.user_base4(self.file_name,self.file_name2)


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case.html")
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_changepasword'))
    suite.addTest(FirstCase('test_login_changepaypasword'))
    suite.addTest(FirstCase('test_login_bindingcode'))1
    # unittest.TextTestRunner().run(suite)
    # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="report", description=u"测试报告", verbosity=2)
    runner.run(suite)

