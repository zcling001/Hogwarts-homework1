import pytest
import requests

from hw0307 import get_datas
from test_requests.rep_page.base import Base


class Contact(Base):

    # 批量删除人员
    def delete_members(self, useridlist):
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete'
        delete_useridlist_data = {"useridlist": useridlist}
        r = self.s.post(url=delete_member_url, json=delete_useridlist_data)
        return r.json()

    # 添加人员
    def add_member(self, userid, name, department, mobile, email):
        add_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        add_members_data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
            "position": "产品经理",
            "gender": "1",
            "email": email}
        r = self.s.post(url=add_member_url, json=add_members_data)
        return r.json()

    # 获取人员信息并删除测试人员角色
    def get_member(self, userid):
        params = {"userid": userid}
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = self.s.get(url=get_member_url, params=params)
        return r.json()


if __name__ == '__main__':
    Contact().add_member()
