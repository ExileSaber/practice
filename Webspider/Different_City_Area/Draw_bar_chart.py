import matplotlib
import numpy as np
import matplotlib.pyplot as plt


# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号


def draw_bar_chart(Xiaoqu_list, KEYWORD, name):
    if name == 'spider_popular_village':
        House = []
        Price = []
        for i in range(len(Xiaoqu_list)):
            K = Xiaoqu_list[i].keys()
            Key = list(K)
            House.append(Key[0])
            Price.append(Xiaoqu_list[i][Key[0]])

        bar_positions = np.arange(len(House)) + 1
        tick_positions = range(1, len(House)+1)
        fig, ax = plt.subplots()

        ax.bar(bar_positions, Price, 0.5)
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(House, rotation=45)

        ax.set_xlabel('小区名')
        ax.set_ylabel('价格（元/平方米）')
        string = KEYWORD + '市热门小区价位比较'
        ax.set_title(string)
        plt.savefig(string + '.jpg')
        plt.show()

    elif name == 'spider_recommend_village':
        House = []
        Price = []
        for i in range(len(Xiaoqu_list)):
            K = Xiaoqu_list[i].keys()
            Key = list(K)
            House.append(Key[0])
            Price.append(Xiaoqu_list[i][Key[0]])

        for i in range(3):
            plt.rcParams['figure.figsize'] = (12.0, 6.0)
            bar_positions = np.arange(10) + 1
            tick_positions = range(1, 11)
            fig, ax = plt.subplots()
            rects = ax.bar(left=bar_positions, height=Price[10*i:10*i+10], width=0.5)
            ax.set_xticks(tick_positions)
            ax.set_xticklabels(House[i*10:i*10+10], rotation=35)

            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")

            ax.set_xlabel('小区名')
            ax.set_ylabel('价格（元/平方米）')
            string = KEYWORD + '市推荐小区价位比较' + '_' + str(i+1)
            ax.set_title(string)
            plt.savefig(string + '.jpg')
        plt.show()

    elif name == 'spider_by_fangjia':
        Place = []
        Price = []

        for i in range(len(Xiaoqu_list)):
            K = Xiaoqu_list[i].keys()
            Key = list(K)
            Place.append(Key[0])
            Price.append(Xiaoqu_list[i][Key[0]])

        plt.rcParams['figure.figsize'] = (12.0, 6.0)
        bar_positions = np.arange(len(Place)) + 1
        tick_positions = range(1, len(Place) + 1)
        fig, ax = plt.subplots()
        rects = ax.bar(left=bar_positions, height=Price, width=0.5)
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(Place, rotation=35)

        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")

        ax.set_xlabel('小区名')
        ax.set_ylabel('价格（元/平方米）')
        string = KEYWORD + '市部分区域价位比较'
        ax.set_title(string)
        plt.savefig(string + '.jpg')
        plt.show()

    elif name == 'spider_by_ditu':
        Place = []
        Price = []

        for i in range(len(Xiaoqu_list)):
            K = Xiaoqu_list[i].keys()
            Key = list(K)
            Place.append(Key[0])
            Price.append(Xiaoqu_list[i][Key[0]])

        plt.rcParams['figure.figsize'] = (12.0, 6.0)
        bar_positions = np.arange(len(Place)) + 1
        tick_positions = range(1, len(Place) + 1)
        fig, ax = plt.subplots()
        rects = ax.bar(left=bar_positions, height=Price, width=0.5)
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(Place, rotation=35)

        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")

        ax.set_xlabel('小区名')
        ax.set_ylabel('价格（元/平方米）')
        string = KEYWORD + '市各区域价位比较'
        ax.set_title(string)
        plt.savefig(string + '.jpg')
        plt.show()
