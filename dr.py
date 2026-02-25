#eval用法
# a=input()
# b=eval(a)*2
# print(b)

# a=eval(input("请输入数字："))*2
# print(a)
#倒叙输出
# a=input("请输入一段文本：")
# print(a[::-1])

# n=int(input("请输入一个整数N："))
# sum=0
# for i in range(n):
#     sum=sum+i
# print(f"1到N求和结果：{sum}")

# n=int(input("请输入一个整数N："))
# add=n**32
# print(add)
# n=int(input("请输入一个整数："))
# add=n*2
# print(add)
#字符串的格式控制
# s="abcdef"
# print("{:*^20}".format(s))
# print("{:$^20}".format(s))
#先用引号包括,再用大括号包裹,之后是:,填充字符,对齐方式,设定的宽度,之后再format
# a="123"
# b="-"
# c="^"
# print("A {0:{1}{3}{2}} A".format(a,b,20,c))
#逗号是千位分隔符
# print("{1:-^25,}".format(12345,90345))
# print("{:-^25,}".format(12345,90345))
# print("{:-^30,.2f}".format(12345.6789))
# print("{:.5}".format("全国计算机考试"))
# print("{0:b},{0:o},{0:c},{0:X}".format(425))
# s=chr(0x2708)
# print(s)
# s="王蕊大王万岁"
# print(f'{s}'.center(20,"$"))
# print(f'{s}'.count('王'))
# print(",".join(['6','7','8']))