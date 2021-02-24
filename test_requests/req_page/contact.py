from test_requests.req_page.base import Base
class Contact(Base):
    def create_member(self,userid,name,department,mobile,**kwargs):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
        }
        data.update(kwargs)
        add_member_response = self.s.post(url=url, json=data)
        return add_member_response.json()
    def find_member(self, userid):
        params = {"userid": userid}
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = self.s.get(get_member_url, params=params)
        return r.json()

    def delete_member(self,userid):
        params = {"userid": userid}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        delete_member_response = self.s.get(url,params=params)
        return delete_member_response.json()