import pytest

from test_requests.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.userid = "hello00123"
        self.name = "hello_today"

    @pytest.mark.parametrize("corpid, corpsecret, result",
                             [(None, None, 0), ('xxx', None, 40013), (None, 'xxx', 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get('errcode') == result

    def test_create(self):

        self.contact.create_member(userid=self.userid, name=self.name, mobile="13866666766", department=[1], alias="xxxxx")
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result["name"] == self.name
