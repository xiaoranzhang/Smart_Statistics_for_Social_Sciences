# !/usr/bin/python
# _*_ coding:utf-8 _*_

# 加载模块
import math


# class Correlation_function:
# 获得每个输入数的函数
def input_list(n):
    '''
    这个函数用于生成输入的数据的数组。
    每输入一个数据，就加入数组input_data中。
    '''
    input_data=[]
    #sum_n = 0
    for i in range(0,n):
        i_n=int(raw_input("输入数据："))
        input_data.append(i_n)
    #print input_data
    return input_data

# 遍历数组，并计算数组元素之和的函数
def list_sum():
    '''
    调用input_list()函数的返回值：加入数据的数组。
    这个函数主要用于遍历input_list()函数中的数组input_data。
    从而取出数组input_data中的每一个数据，并计算数组元素中的和。
    '''
    sum_n=0
    global input_list    # 全局变量
    result_func_input_list=input_list(n)    # 调用函数input_list()
    for j in result_func_input_list:
        global sum_n    # 全局变量
        sum_n=sum_n+j
    #print 'sum:',sum_n
    return sum_n

# 平均数函数：
def average(n):
    '''
    计算输入所有数据的平均数。
    这个函数是程序入口所调用的第一个函数。
    '''
    global list_sum    # 全局变量
    result_func_list_sum=list_sum()    # 调用函数list_sum()
    aver= 1/(n-1) * result_func_list_sum    # !!!!!!!!!!!
    #print 'aver',aver
    return aver    # 如果不使用math模块，除法之后的结果会出错（注意！！此处没有调用math模块。update:6/29）


# 标准计分函数：
#def standard_score():
    #pass


# 程序入口：
n= int(raw_input("请输入要计算的数据个数(n)："))    # 输入要计算的数据个数
average(n)    # 调用第一个函数 average()

if __name__ == "__main__":
    # 调试
    print_func_input_list=input_list(n)
    print_func_list_sum=list_sum()
    print_func_average=average(n)
    print "input_list:", print_func_input_list
    print "list_sum:", print_func_list_sum
    print "average:", print_func_average