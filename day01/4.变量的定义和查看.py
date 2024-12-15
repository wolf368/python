'''
python语言在定义变量时，不需要指定变量的数据类型，python程序会根据
变量的值，自动实现变量类型的确定

python语言：num1=10->num1是int类型
c语言 int num1=10

python数据类型
格式：
    变量名=变量值

1.整形类型 int（integer）
num1=99
print(f''={num1}) 输出的固定格式 f -> format格式化，特点就是在单引号字符串中能书写{}
大括号中可以放入变量名，输出变量值

查看变量的类型：type(变量名)
'''

# "="赋值运算符 从右向左看
name='玛利亚'
# 将“玛利亚”存储到名为“name”的盒子
num1=99
print(f'num1={num1},type(num1)={type(num1)}')
"""
 没有f这个符号，单引号中的{}就无作用
 作用是将变量名对应的变量值输出
 
 num1=999,type{num1}=class 'int'
                     类型   整型

"""