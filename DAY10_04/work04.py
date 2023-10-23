def remove_duplicates_and_convert_to_tuple(lst):
    unique_list = list(set(lst))
    unique_tuple = tuple(unique_list)
    return unique_tuple

# 示例用法
my_list = [1, 2, 3, 4, 2, 2, 3, 4, 4, 4]
new_tuple = remove_duplicates_and_convert_to_tuple(my_list)
print(new_tuple)