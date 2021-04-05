import requests
from requests import Session


class Base:

    def __init__(self):
        self.s = Session()
        self.corpid = "wwb1f41b9d378f61a6"
        self.corpsecret = "fCco872UfsJ31LozgFcefF5jzW-wNx0_RrSvmSwdSDU"
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid == None:
            corpid = self.corpid
        if corpsecret == None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        return r.json()
