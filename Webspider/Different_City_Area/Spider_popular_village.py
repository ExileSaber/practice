from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




def spider_popular_village(KEYWORD):
    '''
    :return:
    -- Xioaqu_list  爬取到的各热门小区各信息组成的字典组成的列表
    '''

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

    js = 'document.getElementById("xiaoqu").display="block";'
    browser.execute_script(js)

    Xiaoqu = browser.find_elements_by_css_selector('.menu li')[3]
    # Xiaoqu = browser.find_element_by_class_name('menu').find_elements_by_tag_name('li')[3]
    Xiaoqu.click()  # 切换到小区搜索方式

    input_xiaoqu = browser.find_element_by_class_name('text.md.txt')
    input_xiaoqu.click()  # 试热度高的小区的display属性改为block

    xiaoqu_html = browser.find_element(By.CLASS_NAME, 'list').find_elements_by_xpath('//li/a')

    xiaoqu_name = []  # 储存要搜索热度高的小区名称
    Xiaoqu_list = []

    # 获取热度高的小区的信息并以字典形式保存[1,2,3,4]
    for i in xiaoqu_html[26:34]:
        xq = {}
        browser.switch_to_window(browser.window_handles[0])
        name = i.text
        xiaoqu_name.append(name)  # 转换为小区名的字符串
        i.click()
        browser.switch_to_window(browser.window_handles[-1])  # 切换到最后一个窗口

        # 获取各项信息
        price = browser.find_element_by_class_name('xiaoquUnitPrice')  # 获取价格
        xq[name] = price.text

        one = browser.find_elements_by_class_name('xiaoquInfoLabel')
        two = browser.find_elements_by_class_name('xiaoquInfoContent')

        for i in range(len(one)):
            xq[one[i].text] = two[i].text

        Xiaoqu_list.append(xq)
        browser.close()
    # 已经获得数据Xiaoqu_list

    # print(Xiaoqu_list)  # 测试结果是否正确

    for i in range(len(Xiaoqu_list)):
        K = Xiaoqu_list[i].keys()
        Key = list(K)
        Xiaoqu_list[i][Key[0]] = int(Xiaoqu_list[i][Key[0]])
        Xiaoqu_list[i][Key[1]] = int(Xiaoqu_list[i][Key[1]][:4])
        Xiaoqu_list[i][Key[-3]] = int(Xiaoqu_list[i][Key[-3]][:-1])
        Xiaoqu_list[i][Key[-2]] = int(Xiaoqu_list[i][Key[-2]][:-1])
    # 对Xiaoqu_list中数据处理一下


    browser.quit()
    print(Xiaoqu_list)  # 测试结果是否正确
    return Xiaoqu_list

# 测试输出
if __name__ == '__main__':
    spider_popular_village('北京')


