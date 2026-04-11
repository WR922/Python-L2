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
# hob=""
# for i in range(3):
#     s=input("请输入你的小爱好（最多三个，按Q结束）：")
#     if s.upper()=='Q':
#         break
#     hob=hob+s+','
# print('你的小爱好是：',hob)
# s=input()
# ss=s.split()
# for i in range(eval(ss[1])):
#   add='Q'*eval(ss[0])
#   print(add)
# for j in range(eval(ss[0])):
#   ad='Q'*(eval(ss[0])+eval(ss[2]))
#   print(ad)
# s=input().strip()
# count=0
# i=0
# while i<=len(s)-3:
#     ad={'b', 'q', 'l'}
#     add=set(s[i:i+3])
#     if add==ad:
#       count+=1
#       i+=3
#     else:
#       i+=1
# print(count)
# def mien(n,base):
#   s=0
#   while n>0:
#     s+=n%base
#     n=n // base
#   return s
# count=0
# for n in range(1,2025):
#   if mien(n,2)==mien(n,4):
#     count+=1
# print(count)
# from datetime import datetime,timedelta
# ji=datetime(1970,1,1,0,0,0)
# t=int(input())
# for _ in range(t):
#     parts=input().split()
#     time_str=parts[0]+' '+parts[1]
#     x=int(parts[2])
#     dt=datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S')
#     total=(dt-ji).total_seconds()
#     total_minute=total//60
#     end_time=ji+timedelta(minutes=total_minute)
#     print(end_time.strftime('%Y-%m-%d %H:%M:%S'))
#示例：
# 2
# 2016-09-07 18:24:33 10
# 2037-01-05 01:49:43 30
# from datetime import date
# def add(a,b,c,d,e,f):
#     d1=date(a,b,c)
#     d2=date(d,e,f)
#     return abs((d2-d1).days)
# print(add(2024,4,2,2025,3,5))
# from datetime import date
# def add(a,b,c):
#     return date(a,b,c).isoweekday()
# print(add(1,2,5))
# s=int(input())
# if (s%4==0 and s%100!=0) or s%400==0:
#     print(f'{s}是闰年')
# else:
#     print(f'{s}不是闰年')
# def add(y,m):
#     if m in [1,3,5,7,8,10,12]:
#         return 31
#     elif m in [4,6,9,11]:
#         return 30
#     else:
#         return 29 if (y%4==0 and y%100!=0) or y%400==0 else 28
# print(add(2004,2))
