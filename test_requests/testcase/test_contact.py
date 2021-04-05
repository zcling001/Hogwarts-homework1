import pytest

from test_requests.rep_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()

    @pytest.mark.parametrize("corpid,corpsecret,result",
                             [(None, None, 0), ('rtytyuiui', None, 40013), (None, "456", 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        print(corpid, corpsecret)
        assert r.get("errcode") == result

    @pytest.mark.parametrize("userid,name,department,mobile, email",
                             [("zzz01", "zzz", [4], "13300001111", "zzz008@gzdev.com")])
    def test_add_member(self, userid, name, department, mobile, email):
        r = self.contact.add_member(userid, name, department, mobile, email)
        print(userid)
        print(name)
        try:
            find_result = self.contact.get_member(userid)
        finally:
            self.contact.delete_members([userid])
        print(find_result)
        assert find_result["name"] == name
