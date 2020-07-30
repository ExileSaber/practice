from selenium import webdriver


def spider_city_allow(url):
    browser = webdriver.Chrome()
    browser.get(url)

    where = browser.find_element_by_class_name('icon-city')
    where.click()
    City = {}
    city = browser.find_elements_by_class_name('city')
    for t in city:
        c = t.find_element_by_tag_name('a')
        key = c.text
        word = c.get_attribute('href')
        City[key] = word

    browser.quit()
    return City


# 测试
# if __name__ == '__main__':
#     city = spider_city_allow('https://bj.5i5j.com/')
#     print(city)
