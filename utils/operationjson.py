from utils.public import *
# from operationExcel import *
from  utils.operationExcel import *
import json

class Operationjson:
    def __init__(self):
        self.excel=OperationExcel()

    def getReadJson(self):
        with open(data_dir(fileName='requestdata.json'),encoding='utf-8') as fp:
            return json.load(fp)

    def get_json_data(self,file='data.xls',row=None):
        '''获取请求参数'''
        return json.dumps(self.getReadJson()[self.excel.get_request_DATA(file,row)])

# opera=Operationjson()
# print(opera.get_json_data(row=11),type(opera.get_json_data(row=11)))

