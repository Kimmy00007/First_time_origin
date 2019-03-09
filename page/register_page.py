#coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

    #获取用户名元素
    def get_name_element(self):
        return self.fd.get_element("user_name")

    #获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")

    #获取密码元素
    def get_password_element(self):
        return self.fd.get_element("password")

    #获取验证码元素
    def get_code_element(self):
        return self.fd.get_element("code_text")

    #获取注册按钮元素
    def get_button_element(self):
        return self.fd.get_element("register_button")

    #获取新密码元素
    def get_newpassword_element(self):
        return self.fd.get_element("new_password")

    #获取确认密码元素
    def get_confirmpassword_element(self):
        return self.fd.get_element("confirm_password")

    #获取vc验证码元素
    def get_vccode_element(self):
        return self.fd.get_element("vccode_text")

    # 获取下一步按钮元素
    def get_nextbutton_element(self):
        return self.fd.get_element("next_button")

    # 获取新支付密码元素
    def get_newpaypassword_element(self):
        return self.fd.get_element("new_paypassword")

    #获取确认支付密码元素
    def get_confirmpaypassword_element(self):
        return self.fd.get_element("confirm_paypassword")

    #获取谷歌验证码元素
    def get_googleCode_element(self):
        return self.fd.get_element("google_Code")