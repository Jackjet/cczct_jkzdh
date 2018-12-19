import unittest
from base.method import Method,IsAssert
from page.zct import *
from page.csrfwr import *
from utils.operationExcel import *
import json
class CcZct(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsAssert()
        self.excel=OperationExcel()

    def statusCode(self,r):
        """正确的返回状态"""
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['statuscode'],1)

    def errstausCode(self,r):
        """错误的返回状态嘛"""
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['statuscode'],-1)

    def test_cczct_001(self):
        '''获取csrf'''
        r=self.obj.get(1)
        csrf=r.headers['Set-Cookie'].split(";")[0]
        # writeheadCsrf(filename='csrf',content=csrf)
        self.excel.get_writexcel(filename='writehead.xls',row=1,col=0,content=csrf)

    def test_cczct_002(self):
        '''验证是否跳转到登录页面'''
        r=self.obj.gethd(2)
        self.assertTrue(self.p.isContent(row=2,str2=r.text))


    def test_cczct_003(self):
        '''输入电话号码点击发送验证码'''
        writefile(filename='phonenumber', content=phonenumber())
        data=get_user_account(3)
        r = self.obj.post(row=3, data=data)
        ci_session = r.headers['Set-Cookie'].split(";")[3].split(", ")[1]
        self.excel.get_writexcel(filename='writehead.xls', row=1, col=1, content=ci_session)
        phone = get_values(4, dict=data)
        if r.json()['statuscode']==1:
            r=self.obj.postci(row=4,data=phone)
        view = r.json()['data']['view_code']
        self.excel.get_writexcel(filename='writehead.xls', row=1, col=2, content=view)
        self.statusCode(r=r)

    def test_cczct_004(self):
        '''输入错误的验证码'''
        r=self.obj.postci(row=5,data=geterr_code(5))
        self.errstausCode(r=r)

    def test_cczct_005(self):
        '''输入正确的验证码'''
        r=self.obj.postci(row=6,data=get_code(6))
        phone = r.json()['data']['phone']
        self.excel.get_writexcel(filename='writehead.xls', row=1, col=3, content=phone)
        self.statusCode(r=r)


    def test_cczct_006(self):
        '''注册后登陆'''
        r=self.obj.postci(7,data=get_zhucdengl(row=7))
        self.assertEqual(r.status_code,200)


    # def test_cczct_007(self):
    #     '''dsadasd'''
    #     r=self.obj.post(8,data=setSo(user_account='18200132292',password='adsadsa',row=8))
    #     print(r.json())
        # self.statusCode(r=r)
        # self.assertTrue(self.p.isContent(row=1,str2=r.text))


if __name__ == '__main__':
    unittest.main(verbosity=2)