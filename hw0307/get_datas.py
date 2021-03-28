import json

import pytest
import yaml


def get_datas():
    with open("../data/data.yml", "rt", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["add_datas"]
        sub_datas = datas["sub_datas"]
        mul_datas = datas["mul_datas"]
        div_datas = datas["div_datas"]
        add_ids = datas["myid"]
        return [add_datas, sub_datas, mul_datas, div_datas, add_ids]


def get_members_datas():
    with open("../data/data_memers.json", "rt", encoding="utf-8") as f:
        json_str = f.read()
        temp = json_str.replace("'", '"')  # 将 单引号 替换为 双引号
        temp = json.loads(temp)  # loads 将 字符串 解码为 字典
        print(temp)


if __name__ == '__main__':
    get_datas()
    print("----------------------------------------------")
    get_members_datas()
