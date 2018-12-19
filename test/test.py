#
# # import itertools
# # # # res=[]
# # # # for i in itertools.permutations(range(1,11),5):
# # # # 	res.append(i[0]*10000+i[1]*1000+i[2]*100+i[3]*10+i[4])
# # # # print(res,len(res))
# # import random
# # def a():
# #     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #     b = random.sample(a, 1)
# #     return b
# #
# # print(a())
import requests

from utils.operationExcel import OperationExcel
OP=OperationExcel()
'''
headers={
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Cookie':'{0}'.format(OP.get_Csrf(file='writehead.xls',row=1)),
            'Referer':'http://orp086.dev.chacha.top/'
        }
data={'user_account':'18161327777','act':'password','password':'adminfkk','reg_url':'http://orp086.dev.chacha.top/'}
r=requests.post(url='http://orp086.dev.chacha.top/user_center/user/login?{0}'.format(OP.get_Csrf(file='writehead.xls',row=1)),data=data,headers=headers)
print(r.json())
'''
'''
headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Cookie':'{0}; {1}'.format(OP.get_Csrf(file='writehead.xls',row=1),OP.get_Ci_Session(file='writehead.xls',row=1)),
            'Referer': 'http://orp086.dev.chacha.top/user/entry'
        }
data={'id':'e0c58f3da952f449d7bd','debug':'1'}
data1={'id':'db8470d18d4e951557fc','debug':'1'}
r=requests.get(url='http://orp086.dev.chacha.top/sup_item',params=data,headers=headers)
print(r.json())
rr=requests.get(url='http://orp086.dev.chacha.top/sup_item',params=data1,headers=headers)
print(rr.json())
#
# def test_var(*arge,**kwargs):
#     for k,v in kwargs.items():
#         print("{0}={1}".format(k,v))
#
# test_var(a=1,b=2,c=3)
'''
import time,datetime
# timeStamp = 1529856000
# timeArray = time.localtime(timeStamp)
# print(timeArray)
# otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
# print(otherStyleTime)
tss1 = '2013-10-10 23:40:00'
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
print(timeArray)
