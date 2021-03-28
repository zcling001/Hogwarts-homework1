'''作业：在天华集团下,
以自己的名字命名一个部门，在部门下面增加5个人员（包括名称、手机号码、性别、邮箱、职务），
修改1个人员的状态为禁用，修改一个人的对外职务为“测试学员”，
获取5个人的信息，删除对外职务为“测试学员”的人员'''
import requests


# coding=utf-8
# 企业ID:wwb1f41b9d378f61a6;
# Secret :fCco872UfsJ31LozgFcefF5jzW-wNx0_RrSvmSwdSDU

# 获取token
def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwb1f41b9d378f61a6&corpsecret=fCco872UfsJ31LozgFcefF5jzW-wNx0_RrSvmSwdSDU')
    # assert 0== r.json()['errcode']
    token = r.json()['access_token']
    return token


# 创建部门
def test_creat_department():
    creat_department_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}'
    creat_department_data = {
        "name": "周翠玲",
        "parentid": 1}
    r = requests.post(url=creat_department_url, json=creat_department_data)
    print(r.json())


# 批量删除人员
def test_delete_members(mebers):
    add_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token={get_token()}'
    creat_body_data = {
        "useridlist": mebers
    }
    r = requests.post(url=add_member_url, json=creat_body_data)
    print(r.json())


def test_delete_all():
    mebers = ["zcl001", "zcl002", "zcl003", "zcl004", "zcl005"]
    test_delete_members(mebers)


# 添加人员
def test_add_members():
    add_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    add_members_datas = [{
        "userid": "zcl001",
        "name": "周翠玲01",
        "department": [4],
        "mobile": "13100000001",
        "position": "产品经理",
        "gender": "1",
        "email": "zcl001@gzdev.com"
    }, {
        "userid": "zcl002",
        "name": "周翠玲02",
        "department": [4],
        "mobile": "13100000002",
        "position": "产品经理",
        "gender": "1",
        "email": "zcl002@gzdev.com"
    }, {
        "userid": "zcl003",
        "name": "周翠玲03",
        "department": [4],
        "mobile": "13100000003",
        "position": "产品经理",
        "gender": "1",
        "email": "zcl003@gzdev.com"
    }, {
        "userid": "zcl004",
        "name": "周翠玲04",
        "department": [4],
        "mobile": "13100000004",
        "position": "产品经理",
        "gender": "1",
        "email": "zcl004@gzdev.com"
    }, {
        "userid": "zcl005",
        "name": "周翠玲05",
        "department": [4],
        "mobile": "13100000005",
        "position": "产品经理",
        "gender": "1",
        "email": "zcl005@gzdev.com"
    }]
    for i in range(0, len(add_members_datas)):
        r = requests.post(url=add_member_url, json=add_members_datas[i])
        print(r.json())


# 修改人员信息
def test_edit_member():
    edit_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    edit_member_data = {
        "userid": "zcl001",
        "position": "测试学员",
        "enable": 0
    }
    r = requests.post(url=edit_member_url, json=edit_member_data)
    print(r.json())


# 获取人员信息
def test_get_memberInformation():
    get_memberInformation_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token={get_token()}&department_id=4&fetch_child=0'
    r = requests.get(url=get_memberInformation_url)
    members = r.json()['userlist']
    for i in range(0, len(members)):
        member = members[i]
        if member['position'] == "测试学员":
            userid = member['userid']
            # 调用批量删除组员接口，注意此处参数是一个数组
            test_delete_members([userid])


if __name__ == '__main__':
    test_creat_department()
