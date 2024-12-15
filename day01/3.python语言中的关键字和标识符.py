# 快速创建python模块：alt+insert
'''
关键字：有些单词被python赋予了特殊含义，不可直接使用
关键字是编程语言里事先定义并被赋予了特殊含义的单词，也成“保留字”
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
  'yield']
python中的关键字共35个

自己定义一些名称：
名称：变量，函数，类型。。。被称为标识符
规则：
1.数字不能开头
2，只能使用a到z A~Z 0~9（下划线），其它符号非法
3.严格区分大小写

命名规范：函数/功能：（坦克撞击墙壁）
1.小驼峰命名规则：tankHitWall
2.大驼峰命名规则：TankHitWall
3.下划线命名规则：tan_hit _wall

全部大写：常量（不会发生变化的数据） PI
'''

# 1.导入系统库
import keyword
# 2.输出查看系统系统的关键字列表
print(keyword.kwlist)
# 3.输出查看系统关键字的总长度
print(len(keyword.kwlist))
