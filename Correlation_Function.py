# !/usr/bin/python
# _*_ coding:utf-8 _*_

# 加载模块
import math


# class Correlation_function:
# 计算X的平均数，标准差，标准计分：
#==============================================================================================
# 获得每个输入数的函数
def input_list_x(n_x):
    '''
    这个函数用于生成输入的数据的数组
    每输入一个数据，就加入数组input_data中
    '''
    input_data_x = []
    #sum_n = 0
    for i in range(0,n_x):
        i_n = int(raw_input("输入数据："))
        input_data_x.append(i_n)
    #print 'input_data_x:', input_data_x
    return input_data_x    # 返回值是数组！！

# 遍历数组，并计算数组元素之和的函数
def list_sum_x():
    '''
    调用input_list()函数的返回值：加入数据的数组
    这个函数主要用于遍历input_list()函数中的数组input_data
    从而取出数组input_data中的每一个数据，并计算数组元素中的和
    '''
    sum_n_x = 0
    #global input_list    # 全局变量
    result_func_input_list_x = input_list_x(n_x)    # 调用函数input_list_x()
    for j in result_func_input_list_x:
        global sum_n_x    # 全局变量
        sum_n_x = sum_n_x + j
    #print 'sum:', sum_n_x
    return sum_n_x

# 平均数函数：
def average_x(n_x):
    '''
    计算输入所有数据的平均数
    这个函数是程序入口所调用的第一个函数
    '''
    #global list_sum    # 全局变量
    result_func_list_sum_x = list_sum_x()    # 调用函数list_sum_x()
    aver_x = 1 / (n_x - 1) * result_func_list_sum_x    # !!!!!!!!!!!
    #print 'aver:', aver_x
    return aver_x    # 如果不使用math模块，除法之后的结果会出错（注意！！此处没有调用math模块。update:6/29）

# 标准差函数
def standard_deviation_x():
    '''
    标准差函数主要用于计算输入的各个数据X的标准差
    需要调用函数average(),以及函数input_list的返回值
    '''
    result_func_average_x = average_x(n_x)
    result_func_input_list_x = input_list_x(n_x)
    inner_brackets = 0
    for s in result_func_input_list_x:    # 取出数组input_data_x中的函数
        global inner_brackets
        inner_brackets = inner_brackets + (s- result_func_average_x) ** 2    # 计算标准差中括号内的数学表达式
    out_brackets = inner_brackets / (n_x - 1)       # 计算方差： [(x1-x)^2+(x2-x)^2+......(xn-x)^2]/(n) （x为平均数）
    stard_devia_x = out_brackets ** 0.5    # 计算标准差（方差的开方） 或者调math模块：math.sqrt()
    #print 'stard_devia:', stard_devia_x
    return stard_devia_x    # 返回标准差数值

# 标准计分函数：
def standard_score_x():
    '''
    这个函数用于计算X的标准计分，并将每个X标准计分结果存入数组standard_score_list中
    '''
    standard_score_list_x = []    # 建立一个空数组，用于存放每个X的标准计分
    result_func_input_list_x = input_list_x(n_x)
    result_func_average_x = average_x(n_x)
    result_func_standard_deviation_x = standard_deviation_x()
    for n_input_x in result_func_input_list_x:    # 遍历input_list_x()函数中的数组
        stard_scr = (n_input_x - result_func_average_x) / result_func_standard_deviation_x    # 标准计分计算公式
        standard_score_list_x.append(stard_scr)
    #print 'standard_score_list:', standard_score_list_x
    return standard_score_list_x    # 返回值是数组！！！


#============================================================================================



# 计算y的平均数，标准差，标准计分：
#============================================================================================
# 获得每个输入数的函数
def input_list_y(n_y):
    '''
    这个函数用于生成输入的数据的数组
    每输入一个数据，就加入数组input_data中
    '''
    input_data_y = []
    #sum_n = 0
    for i in range(0,n_y):
        i_n = int(raw_input("输入数据："))
        input_data_y.append(i_n)
    #print 'input_data_y:', input_data_y
    return input_data_y    # 返回值是数组！！

# 遍历数组，并计算数组元素之和的函数
def list_sum_y():
    '''
    调用input_list()函数的返回值：加入数据的数组
    这个函数主要用于遍历input_list()函数中的数组input_data
    从而取出数组input_data中的每一个数据，并计算数组元素中的和
    '''
    sum_n_y = 0
    global input_list    # 全局变量
    result_func_input_list_y = input_list_y(n_y)    # 调用函数input_list_y()
    for j in result_func_input_list_y:
        global sum_n_y    # 全局变量
        sum_n_y = sum_n_y + j
    #print 'sum:', sum_n_y
    return sum_n_y

# 平均数函数：
def average_y(n_y):
    '''
    计算输入所有数据的平均数
    这个函数是程序入口所调用的第一个函数
    '''
    #global list_sum    # 全局变量
    result_func_list_sum_y = list_sum_y()    # 调用函数list_sum_y()
    aver_y = 1 / (n_y - 1) * result_func_list_sum_y    # !!!!!!!!!!!
    #print 'aver:', aver_y
    return aver_y    # 如果不使用math模块，除法之后的结果会出错（注意！！此处没有调用math模块。update:6/29）

# 标准差函数
def standard_deviation_x():
    '''
    标准差函数主要用于计算输入的各个数据X的标准差
    需要调用函数average(),以及函数input_list的返回值
    '''
    result_func_average_y = average_y(n_y)
    result_func_input_list_y = input_list_y(n_y)
    inner_brackets = 0
    for s in result_func_input_list_y:    # 取出数组input_data_y中的函数
        global inner_brackets
        inner_brackets = inner_brackets + (s- result_func_average_y) ** 2    # 计算标准差中括号内的数学表达式
    out_brackets = inner_brackets / (n_y - 1)       # 计算方差： [(x1-x)^2+(x2-x)^2+......(xn-x)^2]/(n) （x为平均数）
    stard_devia_y = out_brackets ** 0.5    # 计算标准差（方差的开方） 或者调math模块：math.sqrt()
    #print 'stard_devia:', stard_devia_y
    return stard_devia_y    # 返回标准差数值

# 标准计分函数：
def standard_score_y():
    '''
    这个函数用于计算X的标准计分，并将每个X标准计分结果存入数组standard_score_list中
    '''
    standard_score_list_y = []    # 建立一个空数组，用于存放每个X的标准计分
    result_func_input_list_y = input_list_y(n_y)
    result_func_average_y = average_y(n_y)
    result_func_standard_deviation_y = standard_deviation_y()
    for n_input_y in result_func_input_list_y:    # 遍历input_list_y()函数中的数组
        stard_scr = (n_input_y - result_func_average_y) / result_func_standard_deviation_y    # 标准计分计算公式
        standard_score_list_y.append(stard_scr)
    #print 'standard_score_list:', standard_score_list_y
    return standard_score_list_y    # 返回值是数组！！！


#============================================================================================

# 程序入口：
n_x = int(raw_input("请输入要计算的数据个数(n_X) :"))    # 输入要计算的数据个数
standard_score_x()    # 调用第一个函数 standard_score_x()
n_y = int(raw_input("请输入要计算的数据个数（n_Y）:"))
standard_score_y()


# 计算X与Y的标准差乘积——相关系数r：
#============================================================================================




pass






#=============================================================================================

DOC：
'''
x:
y:

x的平均数：
y的平均数：

x的标准差：
y的标准差：

x的标准计分:
y的标准计分：


相关系数r= X与y对应标准差的乘积的平均
'''


if __name__ == "__main__":
    # 调试
    print_func_input_list_x = input_list_x(n_x)
    print_func_list_sum_x = list_sum_x()
    print_func_average_x = average_x(n_x)
    print "input_list:", print_func_input_list_x
    print "list_sum:", print_func_list_sum_x
    print "average:", print_func_average_x

    print_func_input_list_y = input_list_y(n_y)
    print_func_list_sum_y= list_sum_y()
    print_func_average_y = average_y(n_y)
    print "input_list:", print_func_input_list_y
    print "list_sum:", print_func_list_sum_y
    print "average:", print_func_average_y


