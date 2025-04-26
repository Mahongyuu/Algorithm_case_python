import random

# 生成无序数组（100个元素，范围1~1000）
unordered_array = [random.randint(1, 1000) for _ in range(100)]

# 打印前10个元素（避免输出过长）
print("生成的无序数组（前10个元素）:", unordered_array[:10])
print("数组长度:", len(unordered_array))
print(unordered_array)