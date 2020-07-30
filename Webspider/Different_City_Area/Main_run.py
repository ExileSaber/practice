import Draw_bar_chart
import Spider_popular_village
import Spider_recommend_village
import Spider_by_fangjia
import Spider_by_ditu
import Write_in_mongoDB

KEYWORD = input("你要查询的地区：")
WAY = ['spider_popular_village', 'spider_recommend_village', 'spider_by_fangjia', 'spider_by_ditu']
NUMBER = int(input("采用的方法的编号："))
way = WAY[NUMBER]

if NUMBER == 0:
    popular_village = Spider_popular_village.spider_popular_village(KEYWORD)
    save = input("是否需要存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(popular_village, KEYWORD, way)
    else:
        pass
    draw = input("是否需要绘制条形图：")
    if draw == '是':
        Draw_bar_chart.draw_bar_chart(popular_village, KEYWORD, way)
    else:
        pass

elif NUMBER == 1:
    recommend_village = Spider_recommend_village.spider_recommend_village(KEYWORD)
    save = input("是否需要存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(recommend_village, KEYWORD, way)
    else:
        pass
    draw = input("是否需要绘制条形图：")
    if draw == '是':
        Draw_bar_chart.draw_bar_chart(recommend_village, KEYWORD, way)
    else:
        pass


elif NUMBER == 2:
    by_fangjia = Spider_by_fangjia.spider_by_fangjia(KEYWORD)
    save = input("是否需要存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(by_fangjia, KEYWORD, way)
    else:
        pass
    draw = input("是否需要绘制条形图：")
    if draw == '是':
        Draw_bar_chart.draw_bar_chart(by_fangjia, KEYWORD, way)
    else:
        pass

elif NUMBER == 3:
    by_ditu = Spider_by_ditu.spider_by_ditu(KEYWORD)
    save = input("是否需要存入数据库：")
    if save == '是':
        Write_in_mongoDB.write_in_mongoDB(by_ditu, KEYWORD, way)
    else:
        pass
    draw = input("是否需要绘制条形图：")
    if draw == '是':
        Draw_bar_chart.draw_bar_chart(by_ditu, KEYWORD, way)
    else:
        pass

else:
    print('Error, The number is out of the list')
    exit(-1)
