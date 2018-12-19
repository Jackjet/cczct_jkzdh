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

    def statusCode(self, r):
        """正确的返回状态"""
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['statuscode'], 1)

    def errstausCode(self,r):
        """错误的返回状态嘛"""
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['statuscode'],-1)

    def errstausCode1(self,r):
        '''错误状态码为-100001'''
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['statuscode'], -100001)

    def test_dengl_001(self):
        '''输入未注册的手机号，密码登录'''
        r=self.obj.post(row=8,data=setSo(user_account='18161328888',password='adminfkk',row=8))
        self.errstausCode(r=r)

    def test_dengl_002(self):
        '''输入错误格式的手机号，密码登录'''
        r = self.obj.post(row=8, data=setSo(user_account='1816132888', password='adminfkk', row=8))
        self.errstausCode1(r=r)


    def test_dengl_003(self):
        '''输入正确的手机号，密码错误'''
        r = self.obj.post(row=8, data=setSo(user_account='15002803902', password='adminfkk1', row=8))
        self.errstausCode(r=r)


    def test_dengl_004(self):
        '''输入正确的手机号以及密码'''
        r = self.obj.post(row=8, data=setSo(user_account='15002803902', password='adminfkk', row=8))
        self.statusCode(r=r)