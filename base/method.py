import requests
import json
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationjson import Operationjson
from page.csrfwr import *

operation=OperationExcel()

def isurl(row):
    '''判断url里是否包含？号'''
    newurl=operation.get_URL(file='data.xls',row=row)
    if "?" in operation.get_URL(file='data.xls',row=row):
        # newurl=operation.get_URL(row=row)+readheadCsrf('csrf')
        newurl = operation.get_URL(file='data.xls',row=row) +operation.get_Csrf('writehead.xls',1)
    else:
        pass
    return newurl


class Method:
    def __init__(self):
        self.excel=OperationExcel()
        self.opertion=Operationjson()
        self.exdata=ExcelVariable()

    def post(self,row):
        try:
            r=requests.post(
                    url=self.excel.get_URL(file='data.xls',row=row),
                    data=self.opertion.get_json_data(row=row),
                    headers=self.excel.getHeaderValue(),
                    timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生错误')


    def post(self,row,data):
        try:
            r=requests.post(
                    url=isurl(row=row),
                    data=data,
                    headers=self.excel.getHeaderValue(),
                    timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生错误')

    def postci(self,row,data):
        try:
            r=requests.post(
                    url=isurl(row=row),
                    data=data,
                    headers=self.excel.getHeaderValueci(),
                    timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生错误')

    def get(self,row,params=None):
        '''get请求时没有headers头信息'''
        try:
            r=requests.get(
                    url=self.excel.get_URL(file='data.xls',row=row),
                    params=params,
                    headers=None,
                    timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生错误')


    def gethd(self,row,params=None):
        '''get请求时有header头信息带上csrf'''
        try:
            r = requests.get(
                url=self.excel.get_URL(file='data.xls',row=row),
                params=params,
                headers=self.excel.getHeaderValue(),
                timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生错误')

    def get_csrf_ci(self,row,params=None):
        '''get请求header头信息带上csrf,session'''
        try:
            r = requests.get(
                url=self.excel.get_URL(file='data.xls',row=row),
                params=params,
                headers=self.excel.getHeaderValueci(),
                timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生错误')


class IsAssert:
    def __init__(self):
        self.excel=OperationExcel()
    def isContent(self,row,str2):
        flag=None
        if self.excel.get_Expect(file='data.xls',row=row) in str2:
            flag=True
        else:
            flag=False
        return flag

    def isContentall(self,*args,str2):
        flag=None
        for i in args:
            if i in str2:
                flag=True
            else:
                flag=False
            return flag






