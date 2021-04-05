import json

import pytest
import yaml


# E:\pycharm_workspace\Hogwarts-homework1\data\data.yml
def get_datas(file_name=''):
    with open("E:/pycharm_workspace/Hogwarts-homework1/data/" + file_name, "rt", encoding="utf-8") as f:
        if file_name.endswith(".yaml"):
            datas = yaml.safe_load(f)
        elif file_name.endswith(".json"):
            datas = json.load(f)
        else:
            datas = None
        print(datas)
        return datas


if __name__ == '__main__':
    get_datas("data_memers.json")
    # get_members_datas()
