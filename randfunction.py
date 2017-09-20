import random as rd
import os


strABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str123 = '1234567890'
strOther = '!-_'
'''*************************
函数名：getRandString
功能描述：随机返回一个选定的字符
参数：
　　_lstRandSelect：大写字母、小写字母、数字、特殊字符的选择开关，以列表形式保存
　　_strABC：　存放大写字母的函数变量
　　_strabc：　存_strOther放小写字母的函数变量
　　_str123：　存放数字的函数变量
　　_strOther：特殊字符变量



*************************'''

def getRandString(_lstRandSelect,_strABC='',_strabc='',_str123='',_strOther=''):
    if _strABC == '':
        _strABC=strABC
    if _strabc == '':
        _strabc = strABC.lower()
    if _str123 == '':
        _str123 = str123
    if _strOther == '':
        _strOther = strOther

    #所有字符集中在一个list中，方便调用
    lstString = [_strABC,_strabc,_str123,_strOther]
    while True:
        #随机选择一个分类
        iRandSelectClass = rd.randint(0,3)
        if _lstRandSelect[iRandSelectClass] == True:
            break

    #随机从所选的分类中选择一个字符
    iRandSelectNum = rd.randint(0,(len(lstString[iRandSelectClass])-1))
    return(lstString[iRandSelectClass][iRandSelectNum])



# 设置开头为大写字母
def setFirstU(_strPass):
    lstSelect = [True,False,False,False]
    _strPass[0] = getRandString(lstSelect)
    return(_strPass)

# 设置开头为小写字母
def setFirstS(_strPass):
    lstSelect = [False,True,False,False]
    _strPass[0] = getRandString(lstSelect)
    return(_strPass)




#lstRandSelect=[True,True,True,True]
lstRandSelect=[True,True,True,False]
lstPassWord=[]
strPassWord=""
for j in range(10):
    for i in range(8):
        lstPassWord.append(getRandString(lstRandSelect))
    lstPassWord = setFirstU(lstPassWord)
    for k in lstPassWord:
        strPassWord = strPassWord+k
    print(strPassWord)
    lstPassWord=[]
    strPassWord=''
