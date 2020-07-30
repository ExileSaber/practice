from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import quote


def spider_by_fangjia(KEYWORD):
    '''
        :return:
        -- Xioaqu_list  爬取到的各热门小区和其价格组成的字典组成的列表
    '''
    try:
        browser = webdriver.Chrome()  # 构造一个WebDriver对象
        url = 'https://www.lianjia.com/city/'
        browser.get(url)
        input_city = browser.find_element_by_class_name('sug-input')
        input_city.send_keys(KEYWORD)  # send_keys方法用于输入文字
        time.sleep(2)
        # button = browser.find_element_by_class_name('btn')
        # button.click()
        input_city.send_keys(Keys.ENTER)  # 按enter
        # 已经跳转到北京地区
        browser.close()

        browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
        url_2 = browser.current_url
        url = url_2 + quote('fangjia')
        browser.get(url)

        place = []
        price = []
        browser.implicitly_wait(10)
        first = browser.find_elements_by_class_name('circle')

        for f in first:
            place.append(f.find_element_by_class_name('name').text)
            price.append(f.find_element_by_class_name('num').text)

        Place = []
        Price = []
        for i in range(len(place)):
            if place[i] != '' and price[i] != '':
                Place.append(place[i])
                Price.append(int(price[i]))

        Xiaoqu_list = []
        for i in range(len(Place)):
            xq = {}
            xq[Place[i]] = Price[i]
            Xiaoqu_list.append(xq)

    finally:
        browser.close()
        print(Xiaoqu_list)  # 测试
        return Xiaoqu_list

# 测试
# if __name__ == '__main__':
#     spider_by_fangjia()

