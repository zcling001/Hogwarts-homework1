import itertools


# class cartesian(object):
#     def __init__(self):
#         self._data_list = []
#
#     # 添加生成笛卡尔积的数据列表
#     def add_data(self, data=[]):
#         self._data_list.append(data)
#
#     # 计算笛卡尔积
#     def build(self):
#         for item in itertools.product(*self._data_list):
#             print(item)


def runfunc(array0, array1):

    if len(array0) > len(array1):
        longArray = array0
        shortArray = array1
    else:
        longArray = array1
        shortArray = array0

    longArrayLenth = len(longArray)
    shortArrayLenth = len(shortArray)

    # for i in range(longArrayLenth):
    #     for j in range(shortArrayLenth):
    #         if i == j:
    #             print('%d,%d' % (longArray[i], shortArray[i]))
    #         else:
    #             if i >= shortArrayLenth:
    #                 print('%d,%d' % (longArray[i], shortArray[i - shortArrayLenth]))
    #                 break

    for i in range(longArrayLenth):
        print('%d,%d' % (longArray[i], shortArray[i - shortArrayLenth]))


if __name__ == "__main__":
    array0 = [1, 3, 5, 7, 9]
    array1 = [2, 4, 6, 8]
    # array0 = [2, 4, 6, 8]
    # array1 = [1, 3, 5, 7, 9]
    runfunc(array0, array1)
