# encoding=utf-8
import pymysql

db = pymysql.connect(host='localhost',user='root',password='524930lwm',db='house',charset='utf8')
cursor = db.cursor()

#根据操作的不同改变其相应数据
data = {
    'city': '北京', 'house_place': '朝阳', 'id': '500164752', 'href': 'https://bj.5i5j.com/ershoufang/500164752.html', 'title': '板楼带电梯，一梯两户，双卧客厅朝南。', 'house_type': '3室2厅2卫', 'area': '156.62 平米 ', 'toward': ' 南 ', 'floor': ' 低楼层/14层 ', 'fitment': ' 精装 ', 'build_year': ' 2001年建', 'village': '绿荫芳邻', 'other_position': '绿荫芳邻 · 距离地铁望京564米', 'watch_people': '0 人关注 ', 'watch_time': ' 近30天带看 0 次 ', 'release_time': ' 2019-07-03发布', 'all_price': 1100, 'one_price': 70234, 'label': '近地铁，满五年，'
}  #设置你要传入的数据内容
table = 'ershoufang'  #要操作的表格

#不用更改的部分
keys = ','.join(data.keys())  #设置要插入的字段
values = ','.join(['%s']*len(data))  #设置占位符

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)  #sql指令
try:
    if cursor.execute(sql, tuple(data.values())):  #执行操作
        print('Successful')
        db.commit()  #确定更改
except:
    print('Failed')
    db.rollback()  #数据回滚

db.close()
