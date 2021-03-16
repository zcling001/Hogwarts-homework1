import pytest
import yaml

def get_datas():
    with open("D:\python workspace\home_works\Hogwarts-homework1\data\data.yml", "rt", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas=datas["add_datas"]
        sub_datas = datas["sub_datas"]
        mul_datas = datas["mul_datas"]
        div_datas = datas["div_datas"]
        add_ids=datas["myid"]
        return [add_datas,sub_datas,mul_datas,div_datas,add_ids]



if __name__=='__main__':
    get_datas()