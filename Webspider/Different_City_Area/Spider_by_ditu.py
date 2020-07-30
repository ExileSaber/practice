from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains


def spider_by_ditu(KEYWORD):
    '''
        :return:
        -- Xioaqu_list  爬取到的各热门小区各信息组成的字典组成的列表
    '''
    browser = webdriver.Chrome()  # 构造一个WebDriver对象
    url = 'https://www.lianjia.com/city/'
    browser.get(url)
    browser.maximize_window()

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
    url = url_2 + quote('ditu')
    browser.get(url)

    browser.implicitly_wait(10)
    small = browser.find_element_by_class_name('narrow')
    small.click()

    time.sleep(5)  # 还是没能用好显示，隐式等待

    place = []
    price = []
    number = []
    browser.implicitly_wait(10)
    first = browser.find_elements_by_class_name('bubble-2')

    for i in range(len(first)):
        place.append(browser.find_elements_by_class_name('bubble-2')[i].find_element_by_class_name('name').text)
        price.append(browser.find_elements_by_class_name('bubble-2')[i].find_element_by_class_name('num').text)
        number.append(browser.find_elements_by_class_name('bubble-2')[i].find_element_by_class_name('count').text)

    for i in range(len(price)):
        if "万" in price[i]:
            price[i] = float(price[i][:-1]) * 10000
        if "套" in number[i]:
            number[i] = int(number[i][:-1])

    # 去除空项
    Place = []
    Price = []
    Number = []
    for i in range(len(place)):
        if place[i] != '' and price[i] != '' and Number != '':
            Place.append(place[i])
            Price.append(price[i])
            Number.append(number[i])

    Xiaoqu_list = []

    for i in range(len(Place)):
        xq = {}
        xq[Place[i]] = Price[i]
        xq['房屋套数'] = Number[i]
        Xiaoqu_list.append(xq)

    # print(Xiaoqu_list)  # 测试

    # 移动地图，爬取中心区域周围的其他住房
    x = [0, 0, 450, -450]
    y = [450, -450, 0, 0]
    for i in range(4):
        browser.refresh()

        browser.implicitly_wait(10)
        small = browser.find_element_by_class_name('narrow')
        small.click()

        MoveElement = browser.find_element_by_class_name('map')
        time.sleep(3)
        Action = ActionChains(browser)

        # 将鼠标移到MoveElement
        time.sleep(5)
        '''x坐标为正数向右偏移，x坐标为负数向左偏移'''
        '''y坐标为正数向下偏移，y坐标为负数向上偏移'''
        # Action.move_to_element_with_offset(MoveElement, 400, 0).perform()  # 将鼠标移动到距某个元素多少距离的位置
        Action.click_and_hold(MoveElement).perform()
        Action.move_by_offset(x[i], y[i]).perform()  # 鼠标移动到距离当前位置（x,y）
        Action.release(on_element=None).perform()  # 在某个元素位置松开鼠标左键
        time.sleep(5)

        browser.implicitly_wait(10)
        place = []
        price = []
        number = []
        browser.implicitly_wait(10)
        first = browser.find_elements_by_class_name('bubble-2')

        for j in range(len(first)):
            place.append(browser.find_elements_by_class_name('bubble-2')[j].find_element_by_class_name('name').text)
            price.append(browser.find_elements_by_class_name('bubble-2')[j].find_element_by_class_name('num').text)
            number.append(browser.find_elements_by_class_name('bubble-2')[j].find_element_by_class_name('count').text)

        for k in range(len(price)):
            if "万" in price[k]:
                price[k] = float(price[k][:-1]) * 10000
            if "套" in number[k]:
                number[k] = int(number[k][:-1])

        # 去除空项
        Place = []
        Price = []
        Number = []
        for l in range(len(place)):
            if place[l] != '' and price[l] != '' and number[l] != '':
                Place.append(place[l])
                Price.append(price[l])
                Number.append(number[l])

        xq_list = []
        for a in range(len(Place)):

            for b in range(len(Xiaoqu_list)):
                List = list(Xiaoqu_list[b].keys())
                xq_list.append(List[0])
            if Place[a] not in xq_list:
                xq = {}
                xq[Place[a]] = Price[a]
                xq['房屋套数'] = Number[a]
                Xiaoqu_list.append(xq)

    browser.quit()
    print(Xiaoqu_list)  # 测试
    return Xiaoqu_list


# 测试
# if __name__ == '__main__':
#     spider_by_ditu('北京')