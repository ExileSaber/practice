from selenium import webdriver
import time


def spider_place(url):
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    ershoufang = browser.find_element_by_class_name('top-nav').find_element_by_tag_name('li').find_element_by_tag_name(
        'a')
    ershoufang.click()  # 点击了二手房
    browser.close()

    browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口
    time.sleep(2)
    browser.implicitly_wait(10)
    first = browser.find_element_by_class_name('new_di_tab')
    places = first.find_elements_by_tag_name('a')[1:]

    Places = []
    for p in places:
        p.find_element_by_tag_name('li')
        Places.append(p.text)

    # print(Places)
    browser.quit()
    return Places


# 测试
# spider_place('https://bj.5i5j.com/')