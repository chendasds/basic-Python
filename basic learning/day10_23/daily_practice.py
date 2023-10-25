# name = "FakeItEasy"
# length = len(name)
# print(length)
# count = 0
# str1 = "diiaikfka"
# str2 = "sllfla"
# for i in str1:
#     count += 1
# print(count)

# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(count)
#
# str1 = "aooafaa"
# my_len(str1)

# 自动查核酸
# # 函数的声明
# def nucleic_acid():
#     print("欢迎来到应用工程学院")
#     print('请出示48小时的核酸证明')
#
# # 函数的调用
# nucleic_acid()
# 定义函数
# def add(x, y):
#     result = x + y
#     return result
#     print(f"{x} + {y} 的值是{result}")
#
# num = add(4, 5)
# print(num)

# 定义函数
# 升级版自动查核酸
# def nucleic_Acid(num):
#     if num <= 37.3:
#         print(f"您的体温为{num}, 体温正常")
#     else:
#         print(f"您的体温为{num}, 需要隔离")
#
# nucleic_Acid(37.1)

# def nucleic_Acid(num):
#     while num:
#         if num <= 37.3:
#             print(f"{num}, 正常")
#         else:
#             print(f"您的体温为{num}, 需要隔离")
#
# nucleic_Acid(37.1)
# def say_hello():
#     print("hello")
# result = say_hello()
# print(result)
# print(type(result))
def check(age):
    if age > 18:
        return "success"
    else:
        return None
result = check(5)
if not result:
    print("bux")