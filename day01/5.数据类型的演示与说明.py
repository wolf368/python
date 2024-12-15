# 浮点型（小数）float
num2=66.6
print(f'num2={num2},type(num2)={type(num2)}')

#bool 布尔型 -> 只有两种情况，真或者假(Ture/False)
is_visited=True
print(f'is_visited={is_visited},type(is_visited)={type(is_visited)}')

# 字符串类型 -> 有三种格式 1、单引号 2、双引号 3、三引号(多行数据书写)
# 好处：嵌套书写非常简单，不需要转义
# 复制快捷键：ctrl+d
name1='玛利亚'
name2="玛利亚"
name3='''玛利亚'''
name4="""玛利亚"""
print(f'name1={name1},type(name)={type(name1)}')



# pthon中的一些高级数据类型（存储多个数据类型）
# 列表类型
# 特点：有序 可重复 可扩展
names=['张三','李四','王五']
print(f'names={names},type(names)={type(names)}')


# 元组类型：
# 特点：有序，可重复，不可扩展
names=('张三','李四','王五','李四')
print(f'names={names},type(names)={type(names)}')

# 集合类型：
# 特点：无序 不可重复 可扩展
# 无序：内部是通过一套算法决定的，可能使用到了当前时间戳变量
names={'张三','李四','王五','李四'}
print(f'names={names},type(names)={type(names)}')

# 字典类型：key->value 键值对/夫妻对
stud_dict={'stud_id:1001','name:张三','age:18','score:100'}
print(f'stud_dict={stud_dict},type(stud_dict)={type(stud_dict)}')




