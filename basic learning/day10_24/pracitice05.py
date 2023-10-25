# 中文数字对照表
tradition = ("零", "壹", "贰", "叁", "肆", "伍",
                 "陆", "柒", "捌", "玖")
num = input("请输入:")
for i in range(len(num)):
    print(tradition[int(num[i])], "\t", end='')
