import numpy as np
from matplotlib import pyplot as plt


def five_num(data):
    res = [0, 0, 0, 0, 0]
    res[0] = min(data)
    res[1] = np.percentile(data, 25)
    res[2] = np.median(data)
    res[3] = np.percentile(data, 75)
    res[4] = max(data)
    return res


def print_five_num(num):
    print("five number:")
    print("    min:", num[0])
    print("    Q1:", num[1])
    print("    median:", num[2])
    print("    Q3:", num[3])
    print("    max:", num[4])


def print_top_7(data_count):
    # 输出频率前7的元素
    data_sorted = sorted(data_count.items(),
                         key=lambda kv: (kv[1], kv[0]), reverse=True)
    print("top 7:")
    for c in data_sorted[0:7]:
        print(f"    {c[0]}  {c[1]}")


def plt_box(points):
    plt.boxplot(points)
    plt.show()


def plt_bar(data, column):
    points_count = {}
    for row in data:
        if not (row[column] in points_count.keys()):
            points_count[row[column]] = 1
        else:
            points_count[row[column]] += 1
    points_sorted = sorted(points_count.items())
    points_k = [x[0] for x in points_sorted]  # points
    points_v = [x[1] for x in points_sorted]  # count
    plt.bar(points_k, points_v)
    plt.show()


def cal_count(data, column):
    count = {}
    for row in data:
        if not (row[column] in count.keys()):
            count[row[column]] = 1
        else:
            count[row[column]] += 1
    return count


def clean_eliminate(data):
    # 将缺失值剔除
    pass

def clean_fill_freq(data):
    # 填充高频值
    pass

def clean_fill_attr_relation(data):
    # 通过属性相关性填充
    pass

def clean_fill_obj_similarity(data):
    # 通过对象相似性填充
    pass