# !/usr/bin/python
# _*_ coding:utf-8 _*_

import math


#============================================================================================
# 建立输入数据数组的函数：
def input_data_list(n):
    '''
    这个函数用于生成输入的数据的数组
    每输入一个数据，就加入数组input_data[]中
    '''
    data_list = []
    for i in range(0,n):
        input_data = int(raw_input("请输入数据："))
        data_list.append(input_data)
        #input_data.append(i_n)
    #print 'input_data:', input_data
    print "输入数据的数组：", data_list
    return data_list    # 返回值是数组！！


# 输入数据和的函数：
def data_sum(n):
    '''
    调用input_list()函数的返回值：加入数据的数组
    这个函数主要用于遍历input_list()函数中的数组input_data
    从而取出数组input_data中的每一个数据，并计算数组元素中的和
    '''
    sum_n = 0
    #global input_list    # 全局变量
    #result_func_input_data_list = input_data_list(n)    # 调用函数input_list()
    for j in result_func_input_data_list:
        #global sum_n    # 全局变量
        sum_n = sum_n + j
    print "输入数据的和：", sum_n
    return sum_n


# 平均数函数：
def average(n):
    '''
    计算输入所有数据的平均数
    这个函数是程序入口所调用的第一个函数
    '''
    #global list_sum    # 全局变量
    result_func_data_sum = data_sum(n)    # 调用函数data_sum()
    average_means = result_func_data_sum / (n - 1)   # !!!
    print  "输入数据的平均数：", average_means
    return average_means    # average_means = 1/ (n - 1) * result_func_data_sum 这样写程序会出错。（注意！！此处没有调用math模块。update:6/29）


# 标准差函数：
def standard_deviation(n):
    '''
    标准差函数主要用于计算输入的各个数据X的标准差
    需要调用函数average(),以及函数input_list的返回值
    '''
    #result_func_average = average(n)
    #result_func_input_data_list = input_data_list(n)
    inner_brackets = 0
    for i in result_func_input_data_list:    # 取出数组input_data中的函数
        #global inner_brackets
        inner_brackets = inner_brackets + (i - result_func_average) ** 2    # 计算标准差中括号内的数学表达式
    out_brackets = inner_brackets / (n - 1)       # 计算方差： [(x1-x)^2+(x2-x)^2+......(xn-x)^2]/(n) （x为平均数）
    standard_deviation_means = out_brackets ** 0.5    # 计算标准差（方差的开方） 或者调math模块：math.sqrt()
    print  "输入数据的标准差：", standard_deviation_means
    return standard_deviation_means    # 返回标准差数值


# 标准计分函数：
def standard_score():
    '''
    这个函数用于计算X的标准计分，并将每个X标准计分结果存入数组standard_score_list中
    '''
    standard_score_list = []    # 建立一个空数组，用于存放每个X的标准计分
    #result_func_input_list = input_list(n)
    #result_func_average = average(n)
    #result_func_standard_deviation = standard_deviation(n)
    for n_input in result_func_input_data_list:    # 遍历input_list()函数中的数组
        stard_scr = (n_input - result_func_average) / result_func_standard_deviation    # 标准计分计算公式
        standard_score_list.append(stard_scr)
    print "输入数据的标准计分：", standard_score_list
    return standard_score_list    # 返回值是数组！！！


#============================================================================================

# 程序入口 1：
n=int(raw_input('input X的个数:'))
result_func_input_data_list = input_data_list(n)
result_func_average = average(n)
result_func_standard_deviation = standard_deviation(n)
x_result_func_standard_score = standard_score()


n=int(raw_input('input Y的个数:'))
result_func_input_data_list = input_data_list(n)
result_func_average = average(n)
result_func_standard_deviation = standard_deviation(n)
y_result_func_standard_score = standard_score()


# 计算X与Y的标准差乘积的平均——相关系数r以及r方:
#============================================================================================

# 相关系数r的函数：
def correlation_coefficient_r(n):
    '''
    相关系数r= X与y对应标准差的乘积的平均
    '''
	inner_brackets_r = 0
	for x in x_result_func_standard_score:
		for y in y_result_func_standard_score:
			inner_brackets_r = inner_brackets + (x * y)
	r = inner_brackets_r / (n - 1)
	print "相关性系数r：", r
	return r


#=============================================================================================

# 调用程序：
# 程序入口 2：

correlation_coefficient_r(n)

# 这一部分可以添加对r值的判断代码。用判断语句来描述变量之间存在何种相关关系


#对相关性系数r的统计学意义描述：
print "1, 正的r值显示变量之间存在正相关关系，负的r值显示变量之间存在负相关关系。"
print "2, r值在-1和+1之间。r值越接近于0，则表示变量之间的相关关系越弱。"
print "3, r检验只能描述两个变量之间的直线相关关系，不能描述两个变量之间的曲线相关关系。"
print "4, 注意异常值。"


#=============================================================================================

#if __name__ == "__main__":
    # 调试
    #print_func_input_list = input_list(n)
    #print_func_list_sum = list_sum()
    #print_func_average = average(n)
    #print "input_list:", print_func_input_list
    #print "list_sum:", print_func_list_sum
    #print "average:", print_func_average

 

