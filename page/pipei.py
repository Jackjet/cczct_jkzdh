from utils.operationjson import Operationjson
from utils.operationExcel import OperationExcel
import json
from utils.public import *
import time,datetime
operation=Operationjson()
excel=OperationExcel()
def get_id():
    '''获取详情信息的id'''
    with open(data_dir(fileName='id'),'r') as f:
        return json.loads(f.read())

def set_query(row=None,query=None):
    '''输入搜索词匹配'''
    dict1 = json.loads(operation.get_json_data(row=row))
    dict1['query'] = query
    return dict1

def set_query_text(row=None,query_text=None):
    '''首页输入查询条件'''
    dict1 = json.loads(operation.get_json_data(row=row))
    dict1['query_text'] = query_text
    return dict1

def set_query_industry(*args,**kwargs):
    '''查询适用行业'''
    for i in args:
        dict1 = json.loads(operation.get_json_data(row=i))
        dict2={k:v for k,v in kwargs.items()}
        dict1['industry']=dict2['industry']
        return dict1

def set_query_debug(*args,**kwargs):
    '''带上debug=1,查询带上发布时间和适用行业'''
    for i in args:
        dict1 = json.loads(operation.get_json_data(row=i))
        dict2 = {k: v for k, v in kwargs.items()}
        dict1['industry'] = dict2['industry']
        dict1['debug']=dict2['debug']
        dict1['text_pub_time']=dict2['text_pub_time']
        return dict1


def set_query_policy_id(*args,policy_id):
    '''详情页面带上policy_id 和debug=1'''
    for i in args:
        dict1 = json.loads(operation.get_json_data(row=i))
        dict1['id']=policy_id
        return dict1


def settime(text_pub_time):
    '''把时间戳变为指定格式的日期'''
    timeArray=time.localtime(text_pub_time)
    otherStyleTime=time.strftime("%Y", timeArray)
    return otherStyleTime


def settimenyr(text_pub_time):
    '''把时间戳变为指定格式的日期'''
    timeArray=time.localtime(text_pub_time)
    otherStyleTime=time.strftime("%Y/%m/%d", timeArray)
    return otherStyleTime


def set_search(*args,**kwargs):
    '''输入查询条件后，翻页带上所有参数'''
    for i in args:
        dict1 = json.loads(operation.get_json_data(row=i))
        dict2={k:v for k,v in kwargs.items()}
        csrf=excel.get_Csrf(file='writehead.xls', row=1).split("=")[1]
        dict1['csrf']=csrf
        dict1['page_no']=dict2['page_no']
        return dict1

def set_a_s(*args,**kwargs):
    '''通知模块，申报状态获取'''
    for i in args:
        dict1 = json.loads(operation.get_json_data(row=i))
        dict2 = {k: v for k, v in kwargs.items()}
        dict1['a_s'] = dict2['a_s']
        return dict1

def set_gov_agen_first(*args,**kwargs):
    '''文件模块，设置发文体系第一级'''
    for i in args:
        dict1 = json.loads(operation.get_json_data(row=i))
        dict2 = {k: v for k, v in kwargs.items()}
        dict1['gov_agen_first'] = dict2['gov_agen_first']
        dict1['text_pub_time'] = dict2['text_pub_time']
        return dict1

# print(settimenyr(1381419600))