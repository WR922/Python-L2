# 根据用户输入的内容输出相应的结果
# name=input("请输入对方的名字：")
# s=input("请输入悄悄话内容：")
# print(f"{name},听我跟你说：{s}")
# 九九乘法表
# for i in range(1,10):
#    for j in range(1,i+1):
#        print(f"{i}*{j}={i*j:2}",end=' ')
#
#    print('')
#同切圆
#import turtle
#turtle.pensize(3)
#turtle.circle(20)
#turtle.circle(40)
#turtle.circle(80)
#turtle.circle(160)
#turtle.circle(-20)
hob=""
for i in range(3):
    s=input("请输入你的小爱好（最多三个，按Q结束）：")
    if s.upper()=='Q':
        break
    hob=hob+s+','
print('你的小爱好是：',hob)
