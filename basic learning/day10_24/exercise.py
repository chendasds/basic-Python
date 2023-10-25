
# 合并两个列表并按逆序排序
li_num1 = [4, 5, 2, 7]
li_num2 = [3, 6]
li_num1.extend(li_num2)
li_num1.sort(reverse=True)
print(li_num1)

# 向元组的最后一个列表中添加一个新元素"h"
tu_num1 = ("p", "y", "t", ["0", "n"])
tu_num1[3].append("h")
print(tu_num1)