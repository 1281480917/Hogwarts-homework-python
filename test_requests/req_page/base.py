import requests
from requests import Session
class Base:
    def __init__(self):
        self.s=Session()
        self.corpid = 'ww15439cad488e610c'
        self.corpsecret = 'Bly_4jl9M9STdZ66VqYe19wKmkKim9Tdlux76EQeo-s'
        self.s.params["access_token"]=self.get_token()["access_token"]
    def get_token(self,corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {"corpid": corpid, "corpsecret": corpsecret}
        token_response = requests.get(url,params=params)
        return token_response.json()