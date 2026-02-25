# for i in range(101):
#
#     if i%7==0 or i//10==7 or i%10==7:
#         continue
#     print(i)
#     i=i+1
# print("{:*^20,.2f}".format(2345.678))
# print("{:x}".format(425))
#获取用户一段文字，进行纵向输出
# add=input("请输入一段文字：")
# for char in add:
#     print(char)
# add=eval(input("请输入一个合法算式："))
# print(add)
# try:
#     add=float(input("请输入一个小数："))
#     print("{:.0f}".format(add))
# except ValueError:
#     print("输入格式错误！")
# try:
#     add=(int(input("请输入一个整数：")))
#     ad=add//100
#     print(ad)
# except ValueError:
#     print("输入格式错误！")
# try:
#     add=input("请输入一个字符串：")
#     ad=add.split()
#     for i in ad:
#         print(i)
# except ValueError:
#     print("输入格式错误！")
# add=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
# num=int(input("请输入表示星期几的数字:"))
# if 1<=num<=7:
#     print(add[num-1])
# else:
#     print("请输入1到七内的数字")
# add=input("请输入一个任意五位的自然数：")
# if len(add) != 5 or not add.isdigit():
#     print("不符合输入要求")
# else:
#     ad=add[::-1]
#     if ad==add:
#         print(f"{add}是回文数")
#     else:
#         print(f"{add}不是回文数")
# try:
#     add=int(input("请输入一个十进制整数："))
#     print("二进制是{0:b},八进制是{0:o},十六进制是{0:x}".format(add))
# except ValueError:
#     print("请根据要求输入！")