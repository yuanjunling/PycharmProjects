#coding=utf-8
from selenium import webdriver
from random import choice
import time,unittest,random,HTMLParser,hashlib,pytesseract
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image
from PIL import ImageEnhance


class Boss(unittest.TestCase):
    def setUp(self):
        u"""设备报修系统"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "http://127.0.0.1:8090/bdm/login.html"
        self.verificationErrors=[]
        self.accept_next_alet=True
    def test_login(self):
        driver = self.driver
        driver.get(self.Boss_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        u'''登录系统'''
        driver.find_element_by_xpath(".//*[@id='rrapp']/div[2]/div[1]/input").send_keys("admin")
        driver.find_element_by_xpath(".//*[@id='rrapp']/div[2]/div[2]/input").send_keys("000000")
        #截取页面全屏
        driver.save_screenshot(r"D:\aa.png")
        # 找到验证码图片
        ele = driver.find_element_by_xpath(".//*[@id='rrapp']/div[2]/div[4]/img")
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        wwwa = 'D:\\apitest' + now + 'ele.jpg'

        # ele.screenshot(wwwa)
        # image = Image.open(wwwa)
        # vcode = pytesseract.image_to_string(image)
        # time.sleep(3)
        # driver.find_element_by_xpath(".//*[@id='rrapp']/div[2]/div[3]/input").send_keys(vcode)
        location = ele.location  # 获取验证码x,y轴坐标
        size = ele.size #获取验证码的长宽
        coderange = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                     int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open(r"D:\aa.png")  # 打开截图
        frame4 = i.crop(coderange)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(r"D:\frame4.png")
        i2 = Image.open(r"D:\frame4.png")
        imgry = i2.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
        i3 = sharpness.enhance(3.0)  # 3.0为图像的饱和度
        i3.save("D:\\image_code.png")
        i4 = Image.open("D:\\image_code.png")
        text = pytesseract.image_to_string(i2).strip()  # 使用image_to_string识别验证码
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='rrapp']/div[2]/div[3]/input").send_keys(text)





