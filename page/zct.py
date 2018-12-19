#-*- coding:utf-8 -*-
from utils.operationjson import Operationjson
from utils.operationExcel import OperationExcel
from utils.public import *
from page.csrfwr import *
import json
import random

operation=Operationjson()
excel=OperationExcel()

def setSo(user_account=None,password=None,row=None):
    '''对账号密码重新赋值'''
    dict1=json.loads(operation.get_json_data(row=row))
    dict1['user_account']=user_account
    dict1['password']=password
    return dict1

def getexist_user(row):

    '''获取已注册手机号'''
    dict1 = json.loads(operation.get_json_data(row=row))
    return dict1

def get_user_account(row):
    '''获取未注册的手机号'''
    dict1=json.loads(operation.get_json_data(row=row))
    list=phonenumberead('phonenumber')
    a=random.sample(list,1)
    dict1['user_account']=a[0]
    return dict1


def get_values(row,dict):
    '''把登陆输入的手机号，赋值给获取验证码接口参加user_account'''
    dict2=json.loads(operation.get_json_data(row=row))
    dict2['user_account']=dict['user_account']
    return dict2

def get_code(row):
    '''获取验证码'''
    dict1=json.loads(operation.get_json_data(row=row))
    dict1['code']=excel.get_ViewCode(file='writehead.xls',row=1)
    return dict1

def geterr_code(row):
    '''获取错误的验证码'''
    dict1 = json.loads(operation.get_json_data(row=row))
    return dict1

def get_zhucdengl(row):
    '''注册完成后登陆参数'''
    dict1 = json.loads(operation.get_json_data(row=row))
    dict1['user_account']=excel.get_Phone(file='writehead.xls',row=1)
    return dict1

# print(type(setSo(user_account='18200132292',password='adsadsa',row=8)))
# # print(get_code(5))