def find_most_frequent(lst):
    max_count = 0
    most_frequent = None

    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            most_frequent = item

    return most_frequent, max_count


# 示例用法
my_list = [1, 2, 3, 4, 2, 2, 3, 4, 4, 4]
most_frequent_item, frequency = find_most_frequent(my_list)
print(f"The most frequent item is {most_frequent_item} with a frequency of {frequency}.")