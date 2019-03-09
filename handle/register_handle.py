#coding=utf-8
from page.register_page import RegisterPage
from util.get_code import GetCode
from util.GoogleKey import GoogleKey
from util.QrcodeData import QrcodeData
class RegisterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p  =  RegisterPage(self.driver)
    #输入用户名
    def send_user_name(self,name):
        self.register_p.get_name_element().send_keys(name)

    # 输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    # 输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self,filename):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(filename)
        self.register_p.get_code_element().send_keys(code)

    #点击登录按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #输入新密码
    def send_new_password(self,newpassword):
        self.register_p.get_newpassword_element().send_keys(newpassword)

    #确认密码
    def send_confirm_password(self,confirmpassword):
        self.register_p.get_confirmpassword_element().send_keys(confirmpassword)

    # 输入vc验证码
    def send_user_vccode(self,filename):
        get_vccode_text = GetCode(self.driver)
        vccode = get_vccode_text.code_online(filename)
        self.register_p.get_vccode_element().send_keys(vccode)

    #点击下一步
    def click_next_button(self):
        self.register_p.get_nextbutton_element().click()

    # 输入新支付密码
    def send_new_paypassword(self, newpaypassword):
        self.register_p.get_newpaypassword_element().send_keys(newpaypassword)

    # 确认支付密码
    def send_confirm_paypassword(self, confirmpaypassword):
        self.register_p.get_confirmpaypassword_element().send_keys(confirmpaypassword)

    #输入谷歌验证码
    def send_google_Code(self,file_name2):
        get_google_data = QrcodeData(self.driver)
        secret = get_google_data.qr_code_secret(file_name2) #解析二维码取得秘钥
        google_Code = GoogleKey.generate_otp(self,secret) #根据约定的密钥计算当前动态密码
        self.register_p.get_googleCode_element().send_keys(google_Code)