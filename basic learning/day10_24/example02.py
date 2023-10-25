
# 商品价格区间设置与排序
list_product = [399, 2369, 539, 288, 109, 749, 235, 190, 99, 1000]
list_sorted = []
list_max = int(input("请输入您要挑选商品的最大值: "))
list_min = int(input("请输入您要挑选商品的最小值: "))
for i in list_product:
    if list_min <= i <= list_max:
        list_sorted.append(i)
print("1. 升序")
print("2. 降序")
flag = int(input("请输入商品的排序方式(1或2): "))
if flag == 1:
    list_sorted.sort()
    print(list_sorted)
if flag == 2:
    list_sorted.sort(reverse=True)
    print(list_sorted)