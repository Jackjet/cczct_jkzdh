import xlrd
from xlutils.copy import copy
from utils.public import *
import itertools
import json

def writefile(filename=None,content=None):
    '''把需要的内容写入到文件里去'''
    with open(data_dir(fileName=filename),'w') as f:
        f.write(content)

def readfile(filename=None):
    '''把写入到文件里的内容读取出来'''
    with open(data_dir(fileName=filename),'r') as f:
        return f.read()

def phonenumber():
    '''随机生成手机号'''
    phone="150028"
    res=[]
    for i in itertools.permutations(range(1,11),5):
        res.append(i[0]*10000+i[1]*1000+i[2]*100+i[3]*10+i[4])
    return json.dumps([phone+str(i) for i in res])


def phonenumberead(filename=None):
    '''把随机生成的电话号码读取出来'''
    with open(data_dir(fileName=filename),'r') as f:
        return json.loads(f.read())

# writeheadCsrf(filename='phonenumber',content=phonenumber())

# print(phonenumberead(filename='phonenumber'))
# writeheadCsrf(filename='test.xls',row=1,col=0,content="asdasdasdsadad")
# writeheadCsrf(filename='test.xls',row=1,col=0,content="fkk")