import unittest
from base.method import Method,IsAssert
from page.pipei import *
from utils.operationExcel import *
from page.csrfwr import *
import json
import time

class CcZct(unittest.TestCase):

    def setUp(self):
        self.obj=Method()
        self.excel=OperationExcel()
        self.p=IsAssert()
    def statusCode(self, r):
        """正确的返回状态"""
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['statuscode'], 1)

    def test_cczct_001(self):
        '''对成都搜索词进行匹配'''
        r=self.obj.get_csrf_ci(row=9,params=set_query(row=9,query='成都'))
        self.statusCode(r=r)
        self.assertEqual(len(r.json()['data']),6)

    def test_cczct_002(self):
        '''首页第一次输入查询条件'''
        r = self.obj.get_csrf_ci(row=10, params=set_query_text(row=10,query_text='广汉'))
        self.assertTrue(self.p.isContent(row=10, str2=r.text))


    def test_cczct_003(self):
        '''全部页面查询条件里带上-使用行业(汽车交通)-和查询关键字--广汉，地区为四川省德阳市广汉市'''
        r = self.obj.get_csrf_ci(row=11, params=set_query_industry(11,industry=18))
        self.assertTrue(self.p.isContentall('广汉','汽车交通',str2=r.text))



    def test_cczct_004(self):
        '''全部页面查询条件里带上-使用行业(电子信息)-和查询关键字--广汉，地区为四川省德阳市广汉市-debug=1'''
        r=self.obj.get_csrf_ci(row=11,params=set_query_debug(11,industry=2,debug=1,text_pub_time=2018))
        alllist = []
        for i in range(len(r.json()['list'])):

            obj_type = int(r.json()['list'][i]['obj_type'])

            if obj_type == 5:
                '''判断是否为扶持条款，url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                sup_item_url= self.obj.get_csrf_ci(row=12, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(sup_item_url.json())

            elif obj_type==2:
                '''判断是否为扶持政策，url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                sup_policy_url=self.obj.get_csrf_ci(row=13, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(sup_policy_url.json())

            elif obj_type==1:
                '''判断是否为宏观，url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                macro_policy_url = self.obj.get_csrf_ci(row=14, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(macro_policy_url.json())

            elif obj_type==3:
                '''判断是否为实施细则，url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                mimple_regu_url = self.obj.get_csrf_ci(row=15, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(mimple_regu_url.json())

            elif obj_type==4:
                '''判断是否为申报通知，url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                announce_url = self.obj.get_csrf_ci(row=16, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(announce_url.json())

            elif obj_type == 6:
                '''判断是否为细则条款，url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                regu_item_url = self.obj.get_csrf_ci(row=17, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(regu_item_url.json())

            elif obj_type == 7:
                '''判断是否为公示信息url地址不一致'''
                policy_id = r.json()['list'][i]['policy_id']
                publicity_url = self.obj.get_csrf_ci(row=17, params=set_query_policy_id(12, policy_id=policy_id))
                alllist.append(publicity_url.json())

        for i in range(len(alllist)):
            settime(int(alllist[i]['detail']['text_pub_time']))
            '''断言详情页面发文时间是否与选择的查询发文时间年一致'''
            self.assertIn(settime(int(alllist[i]['detail']['text_pub_time'])),settimenyr(int(alllist[i]['detail']['text_pub_time'])))
            '''断言详情页面适用地区是否与选择的适用地区一致'''
            self.assertEqual(alllist[i]['detail']['area_name'],'德阳市广汉市')


    def test_cczct_005(self):
        '''首页输入搜索条件后，向下翻页第二页的数据，只传了查询条件全部页面'''
        r=self.obj.get_csrf_ci(row=19,params=set_search(19,page_no=2,query_text='广汉'))
        list=r.json()['data']['list']
        for i in range(len(r.json()['data']['list'])):
              str=''.join('%s' %id for id in list[i].values())
              self.assertTrue(self.p.isContent(row=19, str2=str))
              self.statusCode(r=r)


    def test_cczct_006(self):
        '''切换到扶持模块查询，查看查询结果是否正确，查询条件地区德阳广汉市，条件广汉，使用行业汽车'''
        r = self.obj.get_csrf_ci(row=20, params=set_query_industry(11, industry=18))
        self.assertTrue(self.p.isContentall('德阳市<em>广汉</em>市', '汽车交通', str2=r.text))

    def test_cczct_007(self):
        '''切换到通知模块查询，查看查询结果是否正确，查询条件地区德阳广汉市，条件广汉，申报状态为申报中'''
        r = self.obj.get_csrf_ci(row=21, params=set_a_s(11, a_s=1))
        self.assertTrue(self.p.isContentall('德阳市<em>广汉</em>市', '申报中', str2=r.text))


    def test_cczct_008(self):
        '''切换到通知模块查询，查看查询结果是否正确，查询条件地区德阳广汉市，条件广汉，申报状态为即将申报'''
        r = self.obj.get_csrf_ci(row=21, params=set_a_s(11, a_s=2))
        self.assertTrue(self.p.isContentall('德阳市<em>广汉</em>市', '即将申报', str2=r.text))

    def test_cczct_009(self):
        '''切换到通知模块查询，查看查询结果是否正确，查询条件地区德阳广汉市，条件广汉，申报状态为申报已截止'''
        r = self.obj.get_csrf_ci(row=21, params=set_a_s(11, a_s=3))
        self.assertTrue(self.p.isContentall('德阳市<em>广汉</em>市', '申报已截止', str2=r.text))


    def test_cczct_010(self):
        '''切换到文件模块查询，查看查询结果是否正确，查询条件地区德阳广汉市，条件广汉，发文体系为中央'''
        r = self.obj.get_csrf_ci(row=22, params=set_gov_agen_first(11,gov_agen_first=1,text_pub_time=2018))
        self.assertTrue(self.p.isContentall('德阳市<em>广汉</em>市', '发文时间：2018','中央',str2=r.text))

    def test_cczct_011(self):
        '''切换到文件模块查询，查看查询结果是否正确，查询条件地区德阳广汉市，条件广汉，发文体系为地方'''
        r = self.obj.get_csrf_ci(row=22, params=set_gov_agen_first(11,gov_agen_first=2,text_pub_time=2018))
        self.assertTrue(self.p.isContentall('德阳市<em>广汉</em>市', '发文时间：2018','地方',str2=r.text))










