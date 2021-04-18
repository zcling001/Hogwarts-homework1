import json

import allure
import pytest

from hw0307.get_datas import get_members_datas
from test_requests.rep_page.contact import Contact


@allure.feature('企业微信接口测试用例')
class TestQYWXAdd:
    def setup_class(self):
        self.contact = Contact()

    @allure.story('测试企业微信人员添加接口')
    @pytest.mark.parametrize("url,params", [(get_members_datas("qywx")[0][3], get_members_datas("qywx")[0][6])])
    def test_add_member(self, url, params):
        userid = json.loads(params)["userid"]
        name = json.loads(params)["name"]
        department = json.loads(params)["department"]
        mobile = json.loads(params)["mobile"]
        email = json.loads(params)["email"]
        r = self.contact.add_member(userid, name, department, mobile, email)
        print(r)
        try:
            find_result = self.contact.get_member(userid)
        finally:
            self.contact.delete_members([userid])
        print(find_result)
        assert find_result["name"] == name
