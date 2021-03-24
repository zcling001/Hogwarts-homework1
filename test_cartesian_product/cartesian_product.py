import itertools


class cartesian(object):
    def __init__(self):
        self._data_list = []

    # 添加生成笛卡尔积的数据列表
    def add_data(self, data=[]):
        self._data_list.append(data)

    # 计算笛卡尔积
    def build(self):
        for item in itertools.product(*self._data_list):
            print(item)


# 前5后6
def runfunc0():
    car = cartesian()
    car.add_data([1, 2, 3, 4, 5])
    car.add_data([6, 7, 8, 9, 10, 11])
    car.build()


# 前6后5
def runfunc1():
    car = cartesian()
    car.add_data([6, 7, 8, 9, 10, 11])
    car.add_data([1, 2, 3, 4, 5])
    car.build()


if __name__ == "__main__":
    runfunc0()
    # runfunc1()
