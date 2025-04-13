import random


class QuickSort:
    # 一、随机取值
    def quick_sort_random(self, arr):
        if len(arr) <= 1:
            return arr
        # 从数组长度内随机取一个数字作为基准值
        pivot_idx = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_idx]
        # 左分区
        left = [x for x in arr if x < pivot]
        # 右分区
        right = [x for x in arr if x > pivot]
        # 中位值
        mid = [x for x in arr if x == pivot]
        # 递归左右分区加上中间值，然后返回
        return self.quick_sort_random(left) + mid + self.quick_sort_random(right)

    #    二、三数取中法
    #     选择第一个、中间、最后一个元素的中位数作为基准值
    def median_of_three(self, arr):
        # 初始化’头尾中‘三个数
        first = arr[0]
        last = arr[-1]
        mid = arr[len(arr) // 2]
        # 排序取三个数中位数
        return sorted([first, last, mid])[1]

    def quick_sort_median(self, arr):
        if len(arr) <= 1:
            return arr
        # 取出中位值为基准
        pivot = self.median_of_three(arr)
        # 同上
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        mid = [x for x in arr if x == pivot]
        return self.quick_sort_median(left) + mid + self.quick_sort_median(right)

    # 三、原地排序实现（节省空间）
    # 从quick_sort_inplace函数开始执行
    def partition(self, arr, low, high):
        # 取最后一位为基准值
        pivot = arr[high]
        # 指向小于基准的最后一个位置
        i = low - 1
        for j in range(low, high):
            # 值比对
            if arr[j] <= pivot:
                i += 1
                # 位置调换
                arr[i], arr[j] = arr[j], arr[i]
        # 将基准值放在‘比对后’且‘交换完’的值的后面
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_inplace(self, arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1
        if low < high:
            # 选取pi为分区点
            pi = self.partition(arr, low, high)
            # pi左边分区排序
            self.quick_sort_inplace(arr, low, pi - 1)
            # pi右边分区排序
            self.quick_sort_inplace(arr, pi + 1, high)
            return arr


# 测试
arr = [10, 7, 8, 9, 1, 5]
# 测试一（随机）
print(QuickSort().quick_sort_random(arr))
# 测试二（中间值）
print(QuickSort().quick_sort_median(arr))
# 测试三（原地排序）
print(QuickSort().quick_sort_inplace(arr))
