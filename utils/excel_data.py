from page.csrfwr import *
class ExcelVariable:
    Testid=0
    url=2
    request_data=3
    expect=4
    Result=5
    def get_Testid(self):
        return ExcelVariable.Testid

    def get_url(self):
        return ExcelVariable.url

    def get_request_data(self):
        return ExcelVariable.request_data

    def get_expect(self):
        return ExcelVariable.expect

    def get_Result(self):
        return ExcelVariable.Result

    # def getHeaderValue(self):
    #     '''获取请求头'''
    #     headers={
    #         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    #         'Cookie':'Hm_lvt_6bfb79812491c34bcab8daa8c77ded37=1541416381; Hm_lpvt_6bfb79812491c34bcab8daa8c77ded37=1543539914; {0}'.format(self.get_Csrf(file='writehead.xls',row=1)),
    #         'Referer':'http://orp086.dev.chacha.top/user/register'
    #     }
    #     return headers
    #
    #
    # def getHeaderValueci(self):
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    #         'Cookie': 'Hm_lvt_6bfb79812491c34bcab8daa8c77ded37=1541416381; Hm_lpvt_6bfb79812491c34bcab8daa8c77ded37=1543539914; {0}; {1}'.format(readheadCsrf(filename='csrf'),readheadCsrf(filename='ci_session')),
    #         'Referer': 'http://orp086.dev.chacha.top/user/register'
    #     }
    #     return headers

class ExcelVariablecsrf:
    csrf=0
    ci_session=1
    view_code=2
    phone=3
    def get_csrf(self):
        return ExcelVariablecsrf.csrf

    def get_ci_session(self):
        return ExcelVariablecsrf.ci_session

    def get_view_code(self):
        return ExcelVariablecsrf.view_code

    def get_phone(self):
        return ExcelVariablecsrf.phone

# ex=ExcelVariable()
# print(ex.getHeaderValue())



