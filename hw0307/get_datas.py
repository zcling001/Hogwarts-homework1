import json
import os

import yaml
import pandas
import allure


# E:\pycharm_workspace\Hogwarts-homework1\data\data.yml
def get_datas(file_name=''):
    root_dir = os.path.dirname(os.path.abspath('.'))
    with open(root_dir + "/data/" + file_name, "rt", encoding="utf-8") as f:
        if file_name.endswith(".yaml"):
            datas = yaml.safe_load(f)
        elif file_name.endswith(".json"):
            datas = json.load(f)
        else:
            datas = None
        print(datas)
        return datas


def get_members_datas(sheet_name=''):
    root_dir = os.path.dirname(os.path.abspath('.'))
    excel = pandas.read_excel(root_dir + "/data/qy_wx_api.xlsx",
                              sheet_name=sheet_name)
    data = excel.values
    # 遍历行
    # for rowIndex in range(len(data)):
    #     rowData = data[rowIndex]
    #     for columnIndex in range(len(rowData)):
    #         columnData = rowData[columnIndex]
    #         print(columnData)
    return data


if __name__ == '__main__':
    # get_members_datas(sheet_name="qywx");
    print("")
    # get_datas("data_memers.json")
    # get_members_datas("/Users/lihe/PycharmProjects/Hogwarts-homework1/data/qy_wx_api.xlsx", "qywx")
