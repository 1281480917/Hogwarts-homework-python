import requests
import json

class TestContack:
    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww15439cad488e610c&corpsecret=Bly_4jl9M9STdZ66VqYe19wKmkKim9Tdlux76EQeo-s'
        token_response = requests.get(url)
        token = json.loads(token_response.text)
        print(token)
        return token['access_token']

    def create_member(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_access_token()}'
        data = {
            "userid": "TomBlank",
            "name": "TomBlank",
            "department": "1",
            "mobile": "13567676666",
        }
        add_member_response = requests.post(url=url, json=data)
        # add_member = json.loads(add_member_response.text)
        # print(add_member)
        # assert 'created' in add_member['errmsg']

    def test_delete_member(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_access_token()}&userid=TomBlank'
        delete_member_response = requests.get(url)
        delete_member = json.loads(delete_member_response.text)
        # assert delete_member['errmsg'] == 'deleted'