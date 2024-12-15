# 对输出内容有特殊要求，用占位符
name='小美'
age=18
print(f'我的名字是{name},今年{age},请多多关照！')
# %s 表示字符串占位符
print('我的名字是%s,今年%s,请多多关照！'%(name,age))

#定义整数变量 student_no,输出我的学号是00001
student_no = 1  # 整数类型不能以0开头
# 整型的占位符为%d
# %06d 整数必须是6位数，如果不足6位，用0补齐
print('我的学号是%06d'%(student_no,))
print('我的学号是%06d'%student_no)

# 定义小数price、weight、money，输出苹果单价9.00元/斤，购买了5.00斤，需支付45.00元
price=9.00
weight=5.00
money=price*weight
# %f表示浮点型占位符   %.1f / %.2f 表示保留一位或两位小数
print('苹果单价%.2f元/斤，购买了%.2f斤需支付%.2f元'%(price,weight,money))

# 定义一个小数scale，输出 数据比列是10%
scale=10.00
print(f'数据的比列{scale}%')
# %是python中的特殊字符如果要输出一个%，需要书写%%
print('数据的比例是%.2f%%'%scale)
print('数据的比例是%.2f%%'%(scale,))