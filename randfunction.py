'''文件名：randfunction.py'''
import random as rd
import os


strABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
strabc = 'abcdefghijklmnopqrstuvwxyz'
str123 = '1234567890'
strOther = '~!@#$%^&*()_+{}|?></][\=-`'
lstDefault = [strABC,strabc,str123,strOther]

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
def getRandString(_lstRandSelect,_strABC = strABC,_strabc = strabc,_str123 = str123,_strOther = strOther):
    #所有字符集中在一个list中，方便调用
    lstString = [_strABC,_strabc,_str123,_strOther]
    #若参数为空或None，则将当前参数设置为默认值。
    for i in range(4):
        if lstString[i] == '' or lstString[i] == None:
            lstString[i] = lstDefault[i]
    while True:
        #随机选择一个分类
        iRandSelectClass = rd.randint(0,3)
        if _lstRandSelect[iRandSelectClass] == True:
            break

    #随机从所选的分类中选择一个字符
    iRandSelectNum = rd.randint(0,(len(lstString[iRandSelectClass])-1))
    return(lstString[iRandSelectClass][iRandSelectNum])


'''*************************
函数名：setFirstU
功能描述：设置开头字母小写
参数：
　　_strPass：需要设置的字符串（密码文本）

*************************'''
# 设置开头为大写字母
def setFirstU(_strPass):
    lstSelect = [True,False,False,False]
    _strPass[0] = getRandString(lstSelect)
    return(_strPass)

'''*************************
函数名：setFirstS
功能描述：设置开头字母小写
参数：
　　_strPass：需要设置的字符串（密码文本）

*************************'''
# 设置开头为小写字母
def setFirstS(_strPass):
    lstSelect = [False,True,False,False]
    _strPass[0] = getRandString(lstSelect)
    return(_strPass)


'''*************************
函数名：getRandPass
功能描述：获取完整随机密码
参数：
　　_lstPassCS：密码生成参数，供getRandString函数使用
    _iNum：密码长度

*************************'''

def getRandPass(_lstPassCS,_iNum):
    strPass = ''
    for i in range(_iNum):
        strPass += getRandString(_lstPassCS[0], _lstPassCS[1], _lstPassCS[2], _lstPassCS[3],_lstPassCS[4])
    return strPass


# 测试代码
lstLeft = [(True,False,False,False),None,None,None,'!_-']
lstCenter = [(True,True,True,False),None,None,None,'!_-']
lstRight = [(False,False,False,True),None,None,None,'!_-']
strPassView=""
for i in range(20):
    strLeft = getRandPass(lstLeft,3)
    strCenter = getRandPass(lstCenter, 10)
    strRight = getRandPass(lstRight, 3)
    strPassView = strLeft + strCenter + strRight
    print(strPassView)
