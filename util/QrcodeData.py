# -*- coding:utf-8 -*-

import os
from PIL import Image
from pyzbar import pyzbar
from util.get_code import GetCode
import time
class QrcodeData:
    def __init__(self,driver):
        self.driver = driver
    def get_code_image(self,file_name2):
        self.driver.save_screenshot(file_name2)
        code_element = self.driver.find_element_by_id("qrcode")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name2)
        img = im.crop((left,top,right,height))
        img.save(file_name2)
        time.sleep(1)

    # #解析二维码
    # def decode_qr_code(self,file_name2):
    #     return pyzbar.decode(Image.open(file_name2), symbols=[pyzbar.ZBarSymbol.QRCODE])

    #根据解析二维码的值取秘钥
    def qr_code_secret(self,file_name2):
        if file_name2.startswith("D:/"):
            self.get_code_image(file_name2)
            results = pyzbar.decode(Image.open(file_name2), symbols=[pyzbar.ZBarSymbol.QRCODE])
            if len(results):
                secret = (results[0].data.decode("utf-8"))[-16:]
            return(secret)
        return file_name2


