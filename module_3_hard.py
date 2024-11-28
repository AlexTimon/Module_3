def calculate_nested_sum(info):
    total_sum = 0
    if isinstance(info, int) or isinstance(info, float):
        return info
    elif isinstance(info, str):
        return len(info)
    elif isinstance(info, list):
        for item in info:
            total_sum += calculate_nested_sum(item)
        return total_sum
    elif isinstance(info, tuple):
        for item in info:
            total_sum += calculate_nested_sum(item)
        return total_sum
    elif isinstance(info, set):
        for item in info:
            total_sum += calculate_nested_sum(item)
        return total_sum
    elif isinstance(info, dict):
        for key in info.items():
            total_sum += calculate_nested_sum(key)
        return total_sum
    else:
        return 0
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_nested_sum(data_structure)
print(result)
