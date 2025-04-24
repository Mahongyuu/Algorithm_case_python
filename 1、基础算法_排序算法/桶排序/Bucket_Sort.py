class BucketSort:
    def bucket_sort(self, arr, bucket_size=10):
        # 边界条件
        if len(arr) == 0:
            return arr

        # 确定数据的范围
        # 找出最大和最小值
        max_val, min_val = max(arr), min(arr)
        # 求出需要的‘桶’的个数
        bucket_count = (max_val - min_val) // bucket_size + 1
        # 用列表推导式制造所需要的桶（此用例为5个桶，即5个[]）
        buckets = [[] for _ in range(bucket_count)]

        # 分配数据到桶内
        for num in arr:
            # 寻桶公式（元素减去最小元素再整除桶大小得到桶序号）
            idx = (num - min_val) // bucket_size  # idx即为桶序号
            # 将元素放入对应桶内
            buckets[idx].append(num)

        # 对桶内元素排序（可使用各种排序，此处使用内置排序）
        sorted_arr = []
        for bucket in buckets:
            # extend()方法将可迭代对象添加到末尾
            sorted_arr.extend(sorted(bucket))

        return sorted_arr


# # 测试示例
if __name__ == '__main__':
    arr = [29, 25, 3, 49, 9, 37, 21, 43]
    print('原数组为：\n', arr)
    sorted_arr = BucketSort().bucket_sort(arr)
    print('排序后数组为：\n', sorted_arr)
