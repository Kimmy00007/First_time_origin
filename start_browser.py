#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest

#打开浏览器，输入网址，输入账号、密码
driver = webdriver.Chrome()
driver.get("**********************************")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("username").send_keys("JTZF800003")
driver.find_element_by_id("username2").send_keys("1@163.com")
driver.find_element_by_id("password").send_keys("111111")

#获取验证码截图
driver.save_screenshot("D:/jt.png")
code_element = driver.find_element_by_id("imgsrc")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("D:/jt.png")
img = im.crop((left,top,right,height))
img.save("D:/jt1.png")

#解析验证码截图输入验证码，点击登录
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/jt1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
time.sleep(2)
driver.find_element_by_id("yzm").send_keys(text)
driver.find_element_by_id("send-btn").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div/ul/li[4]/a[4]").click()
driver.find_element_by_xpath("//*[@id='eb_money']").send_keys("2")
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/span").click()
for i in range(5):
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/form/div[2]/div[2]/input").click()
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert.accept()







