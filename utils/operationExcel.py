import xlrd
from xlutils.copy import copy
from utils.excel_data import *
from  utils.public import *
class OperationExcel(ExcelVariable,ExcelVariablecsrf):

    def getExcel(self,file):
        # db=xlrd.open_workbook(data_dir(fileName='data.xls'))
        db = xlrd.open_workbook(data_dir(fileName=file))
        sheet=db.sheet_by_index(0)
        return sheet

    def get_rows(self,file):
        '''获取所有的行'''
        return self.getExcel(file).nrows


    def get_row_cel(self,file,row,col):
        ''' 获取单元格内容'''
        return self.getExcel(file).cell_value(row,col)

    def get_URL(self,file,row):
        '''获取请求地址'''
        return self.get_row_cel(file,row,self.get_url())

    def get_request_DATA(self,file,row):
        '''获取请求参数'''
        return self.get_row_cel(file,row,self.get_request_data())

    def get_Expect(self,file,row):
        '''获取时间实际结果'''
        return self.get_row_cel(file,row,self.get_expect())

    def get_writexcel(self,filename=None,row=None,col=None,content=None):
        '''对wxcel表的写入'''
        work = xlrd.open_workbook(data_dir(fileName=filename))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(data_dir(fileName=filename))

    def get_Csrf(self,file,row):
        '''获取csrf'''
        return self.get_row_cel(file,row, self.get_csrf())

    def get_Ci_Session(self,file,row):
        '''获取session'''
        return self.get_row_cel(file, row, self.get_ci_session())

    def get_ViewCode(self,file,row):
        '''获取验证码'''
        return self.get_row_cel(file, row, self.get_view_code())

    def get_Phone(self,file,row):
        '''获取电话号码'''
        return self.get_row_cel(file, row, self.get_phone())

    def getHeaderValue(self):
        '''获取请求头'''
        headers={
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Cookie':'{0}'.format(self.get_Csrf(file='writehead.xls',row=1)),
            'Referer':'http://orp086.dev.chacha.top/'
        }
        return headers


    def getHeaderValueci(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Cookie':'{0}; {1}'.format(self.get_Csrf(file='writehead.xls',row=1),self.get_Ci_Session(file='writehead.xls',row=1)),
            'Referer': 'http://orp086.dev.chacha.top/user/entry'
        }
        return headers


# opera=OperationExcel()
# # # # print(opera.get_request_DATA(1))
# # print(opera.getHeaderValueci())