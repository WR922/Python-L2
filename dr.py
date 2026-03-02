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
#求最大公约数
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# def lcm(a,b):
#     return abs(a*b)//gcd(a,b)
# num1=int(input('请输入第一个整数：'))
# num2=int(input('请输入第二个整数：'))
# print(f'{num1}和{num2}的最大公倍数是：{gcd(num1,num2)}')
# print(f'{num1}和{num2}的最小公约数是：{lcm(num1,num2)}')
#读取用户输入的一个字符，统计并输出其中英文字符、数字、空格和其他出现的个数
# w=0
# b=0
# c=0
# d=0
# add=input('请输入一行字符：')
# for a in add:
#     if a.isalpha():
#         w += 1
#     elif a.isdigit():
#         b += 1
#     elif a.isspace():
#         c += 1
#     else:
#         d += 1
# print(f'英文字符{w}个')
# print(f'数字{b}个')
# print(f'空格{c}个')
# print(f'其他字符{d}个')
#输入一个年份，判断是否为闰年，当用户输入的不是整数时，重新输入
def ad(add):
    return (add%4==0 and add%100 !=0 or add%400==0)
while True:
    try:
        add=int(input('请输入一个年份：'))
        if ad(add):
            print(f"{add}是闰年")
        else:
            print(f'{add}年不是闰年')
        break
    except ValueError:
        print('输入内容必须为年份！')
