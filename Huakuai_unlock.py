from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/demo/2017/unlock/")
#定位第一个滑块
dragger = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]

action = ActionChains(driver)
#通过click_and_hold()方法对滑块按下鼠标左键
action.click_and_hold(dragger).perform()  #鼠标左键按下不放

for index in range(200):
    try:
        #接下来就是通过for循环动滑块的位置，
        #move_by_offset()方法:第一个参数是X轴，
        #第二个参数是Y轴，单位为像素。因为是平行移动，
        #所以Y设置为0，X每次移动两2个像素。
        action.move_by_offset(2, 0).perform() #平行移动鼠标
    except UnexpectedAlertPresentException:
        break   #当解锁成功后会抛UnexpectedAlertPresentException异常，捕捉后跳出循环。
    action.reset_actions()  #清除之前的action
    sleep(0.1)  #等待停顿时间

# 打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)
sleep(3)
driver.quit()