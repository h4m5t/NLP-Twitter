# coding:utf-8
import re
import time
from typing import List, Dict
import crawlertool as tool
from Selenium4R import Chrome

class SpiderTwitterAccountInfo(tool.abc.SingleSpider):
    """
    Twitter账号信息爬虫
    """

    def __init__(self, driver):
        self.driver = driver

        # 爬虫实例的变量
        self.user_name = None

    @staticmethod
    def get_twitter_user_name(page_url: str) -> str:
        """提取Twitter的账号用户名称
        主要用于从Twitter任意账号页的Url中提取账号用户名称
        :param page_url: Twitter任意账号页的Url
        :return: Twitter账号用户名称
        """
        if pattern := re.search(r"(?<=twitter.com/)[^/]+", page_url):
            return pattern.group()

    def running(self, user_name: str) -> List[Dict]:
        """执行Twitter账号信息爬虫
        :param user_name: Twitter的账号用户名称（可以通过get_twitter_user_name获取）
        :return: Json格式的Twitter账号数据
        """
        self.user_name = user_name
        actual_url = "https://twitter.com/" + user_name

        self.console("开始抓取,实际请求的Url:" + actual_url)

        self.driver.get(actual_url)
        time.sleep(3)

        item = {}

        if label := self.driver.find_element_by_xpath(
                "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[1]/div/div[5]/div[1]/a"):
            item["following"] = tool.extract.number(label.text)
        elif label := self.driver.find_element_by_xpath(
                "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[1]/div/div[4]/div[1]/a"):
            item["following"] = tool.extract.number(label.text)
        else:
            self.log("Twitter账号:" + user_name + "|账号正在关注数抓取异常")
            item["following"] = 0

        if label := self.driver.find_element_by_xpath(
                "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[1]/div/div[5]/div[2]/a"):
            item["followers"] = tool.extract.number(label.text)
        elif label := self.driver.find_element_by_xpath(
                "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[1]/div/div/div/div/div[1]/div/div[4]/div[2]/a"):
            item["followers"] = tool.extract.number(label.text)
        else:
            self.log("Twitter账号:" + user_name + "|账号粉丝数抓取异常")
            item["followers"] = 0

        return [item]

from selenium import webdriver
# ------------------- 单元测试 -------------------
if __name__ == "__main__":
    
    # r代表后面的字符串斜杠不转义，''表示python识别空格
    # driverOptions.add_argument(r"user-data-dir=C:\Users\loeoe\AppData\Local\Google\Chrome\User''Data\Default\Login''Data")
    
    #初始化webdriver
    driverOptions = webdriver.ChromeOptions()
    
    #导入缓存数据
    driverOptions.add_argument(r"user-data-dir=C:\Users\loeoe\AppData\Local\Google\Chrome\User Data") 

    #对应的chromedriver路径
    driver = webdriver.Chrome(executable_path=r"E:\\Temp\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe",port=0,chrome_options=driverOptions)

    print(SpiderTwitterAccountInfo(driver).running(SpiderTwitterAccountInfo.get_twitter_user_name("https://twitter.com/Doug_Bandow")))
    driver.quit()