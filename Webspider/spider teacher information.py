import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

person_list = []  # 存储所有教师数据的列表

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
url = 'http://www.globalauthorid.com/WebPortal/EliteView?InfoID=d266d50a-e70c-4f31-b0a3-f25b781e3149'

try:
    response = requests.get(url, headers=headers)
    print(response.status_code)  # 输出返回状况，200是正常访问

    # 将一段文档传入BeautifulSoup的构造方法,就能得到一个文档的对象, 可以传入一段字符串
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    # 上卖面两步每次都一样

    # 返回的是class为box1200 mau pd100的<div>标签，之后的输出语句全部注释掉了，需要可以自己查看
    persons = soup.find('div', {'class': 'box1200 mau pd100'})
    # print(persons)

    person_information = persons.find_all('div')  # 从class为box1200 mau pd100的<div>标签中再获取其中全部div子标签
    # print(person_information)

    for div_id, information in enumerate(person_information):
        # print(information)  # 注意这部分是4个div是一个人的信息
        if (div_id + 1) % 4 == 1:
            person_dict = {}  # 创建保存一个教师数据的字典
        if (div_id + 1) % 4 == 1:
            # print(information)
            inf_a = information.find('a')
            if inf_a.text == '首页':
                break  # 跳出循环防治报错
            inf_img = information.find('img')
            # print(ing_img)
            inf_img_src = inf_img.get('src')  # 获取src中的地址
            # print(inf_img_src)
            person_dict['img_src'] = inf_img_src
            # print('-----------img src----------')
        elif (div_id+1) % 4 == 2:
            # print(information)
            inf_text = information.text
            # print(inf_text)
            inf_text = re.split('[ .：\ue628]', inf_text)
            # print(inf_text)  # 分割后有用的部分自己观察
            if len(inf_text) == 9:
                person_dict['name'] = inf_text[1]
                person_dict['school&college'] = inf_text[3]
                person_dict['department1'] = inf_text[4]
                person_dict['college'] = inf_text[5]
                person_dict['department2'] = inf_text[6]
                person_dict['technical title'] = inf_text[7][:-5]

                ORCID = inf_text[8]
                lens = 3
                if len(ORCID) > 10:
                    ORCID = ORCID[:19]
                    lens = 22
                else:
                    ORCID = None
                person_dict['ORCID'] = ORCID
                person_dict['achievement number'] = int(inf_text[8][lens:])

                # print('-----------person----------')
            else:
                person_dict['name'] = inf_text[1]
                person_dict['school&college'] = inf_text[3]
                person_dict['department1'] = inf_text[4]
                person_dict['college'] = inf_text[5]
                person_dict['department2'] = None
                person_dict['technical title'] = inf_text[6][:-5]

                ORCID = inf_text[7]
                lens = 3
                if len(ORCID) > 10:
                    ORCID = ORCID[:19]
                    lens = 22
                else:
                    ORCID = None
                person_dict['ORCID'] = ORCID
                person_dict['achievement number'] = int(inf_text[7][lens:])

                # print('-----------person----------')
        elif (div_id+1) % 4 == 3:  # 后面两部分没用了，就直接这么写了
            person_list.append(person_dict)

except Exception as e:
    print(e)

print(person_list)
