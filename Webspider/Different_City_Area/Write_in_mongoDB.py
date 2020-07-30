import pymongo  # 数据库操作第三方库


client = pymongo.MongoClient(host='localhost', port=27017)  # 链接我电脑上的数据库

def write_in_mongoDB(Xiaoqu_list, keyword, name):
    city = keyword + "房价"
    db = client[city]
    if name == 'spider_popular_village':
        String = 'popular_village'
        collection = db[String]
        flag_1 = 0
        flag_2 = 0
        for xiaoqu in Xiaoqu_list:
            flag_1 = flag_1 + 1
            if collection.insert_one(xiaoqu):
                flag_2 = flag_2 + 1
        print('Popular village saved to Mongo')
        print('一共 ' + str(flag_1) + ' 条数据，存储成功数据条数为：' + str(flag_2))

    elif name == 'spider_recommend_village':
        String = 'recommend_village'
        collection = db[String]
        flag_1 = 0
        flag_2 = 0
        for xiaoqu in Xiaoqu_list:
            flag_1 = flag_1 + 1
            if collection.insert_one(xiaoqu):
                flag_2 = flag_2 + 1
        print('Recommend village saved to Mongo')
        print('一共 ' + str(flag_1) + ' 条数据，存储成功数据条数为：' + str(flag_2))

    elif name == 'spider_by_fangjia':
        String = 'by_fangjia'
        collection = db[String]
        flag_1 = 0
        flag_2 = 0
        for xiaoqu in Xiaoqu_list:
            flag_1 = flag_1 + 1
            if collection.insert_one(xiaoqu):
                flag_2 = flag_2 + 1
        print('Fangjia saved to Mongo')
        print('一共 ' + str(flag_1) + ' 条数据，存储成功数据条数为：' + str(flag_2))

    elif name == 'spider_by_ditu':
        String = 'by_ditu'
        collection = db[String]
        flag_1 = 0
        flag_2 = 0
        for xiaoqu in Xiaoqu_list:
            flag_1 = flag_1 + 1
            if collection.insert_one(xiaoqu):
                flag_2 = flag_2 + 1
        print('Ditu saved to Mongo')
        print('一共 ' + str(flag_1) + ' 条数据，存储成功数据条数为：' + str(flag_2))

