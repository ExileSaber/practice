import Spider_city_allow
import time
import pymysql
import Spider_place
import Spider_all_house

# print('搜集初始数据,leading.......')
# time.sleep(2)
#
# url = 'https://bj.5i5j.com/'  # 进入的初始网址
# City = Spider_city_allow.spider_city_allow(url)
# print(City)
#
# print("搜集完成")
# city = input("输入你要查询的城市：")
City = {'南京': 'https://nj.5i5j.com/'}
city = '南京'

keys = list(City.keys())

if city in keys:
    url_city = City[city]
    Places = Spider_place.spider_place(url_city)
    # Places = Places[11:]

    print(city + "可查询的区域有：", Places)
    number = [12000, 8000, 4000, 4000, 5000, 5000, 2000, 12000, 3, 0, 0]
    # number = number[11:]

    for i in range(len(Places)):
        House_list = Spider_all_house.spider_all_house(url_city, Places[i], number[i], city)

        db = pymysql.connect(host='localhost', user='root', password='524930lwm', db='house_2', charset='utf8')
        cursor = db.cursor()

        table = 'ershoufang'
        for house_dict in House_list:
            keys = ','.join(house_dict.keys())  # 设置要插入的字段
            values = ','.join(['%s'] * len(house_dict))  # 设置占位符

            sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)  # sql指令
            try:
                if cursor.execute(sql, tuple(house_dict.values())):  # 执行操作
                    print('Successful')
                    db.commit()  # 确定更改
            except:
                print('Failed')
                db.rollback()  # 数据回滚

        db.close()


else:
    print("你输入的城市我爱我家网中没有，暂无其他网站可以进行操作")
