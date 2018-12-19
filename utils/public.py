import os
def data_dir(data='data',fileName=None):
    '''对查找文件路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

# print(data_dir(fileName='data.xls') )