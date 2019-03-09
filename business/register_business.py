#coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness:
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)


    def user_base(self,name,email,password,file_name):
        self.register_h.send_user_name(name)
        self.register_h.send_user_email(email)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()

    def user_base2(self,newpassword,confirmpassword,file_name):
        self.register_h.send_new_password(newpassword)
        self.register_h.send_confirm_password(confirmpassword)
        self.register_h.send_user_vccode(file_name)
        self.register_h.click_next_button()

    def user_base3(self,newpaypassword,confirmpaypassword,file_name):
        self.register_h.send_new_paypassword(newpaypassword)
        self.register_h.send_confirm_paypassword(confirmpaypassword)
        self.register_h.send_user_vccode(file_name)
        self.register_h.click_next_button()

    def user_base4(self,file_name,file_name2):
        self.register_h.send_user_vccode(file_name)
        self.register_h.send_google_Code(file_name2)
        self.register_h.click_next_button()