import time


class BucketSort:
    def bucket_sort(self, arr, bucket_size=10):
        """
        桶排序：将数据分配到桶内再对桶内元素调用其他排序方式
        :param arr:
        :param bucket_size:
        :return:
        """
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


start = time.perf_counter()

# # 测试示例
if __name__ == '__main__':
    arr = [373, 862, 836, 578, 413, 755, 694, 306, 916, 612, 889, 262, 58, 846, 711, 826, 248, 955, 43, 221, 501, 901, 638, 728, 397, 442, 377, 976, 513, 309, 323, 411, 564, 900, 368, 882, 639, 722, 738, 791, 473, 785, 202, 266, 364, 678, 860, 995, 290, 422, 720, 37, 495, 475, 722, 432, 218, 310, 311, 412, 733, 802, 68, 524, 124, 713, 5, 652, 274, 203, 789, 862, 788, 695, 858, 654, 347, 315, 562, 479, 77, 278, 153, 340, 332, 650, 649, 845, 993, 552, 787, 619, 799, 710, 779, 257, 266, 454, 882, 746]
    print('原数组为：\n', arr)
    sorted_arr = BucketSort().bucket_sort(arr)
    print('排序后数组为：\n', sorted_arr)
end = time.perf_counter()
print('该程序运行用时为', end - start)
