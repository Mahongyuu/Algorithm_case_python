import random


class QuickSort:
    # 随机取值
    def quick_sort_random(self, arr):
        if len(arr) <= 1:
            return arr
        # 从数组长度内随机取一个数字作为基准值
        povit_idx = random.randint(0, len(arr) - 1)
        povit = arr[povit_idx]
        # 左分区
        left = [x for x in arr if x < povit]
        # 右分区
        right = [x for x in arr if x > povit]
        # 中位值
        mid = [x for x in arr if x == povit]
        # 递归左右分区加上中间值，然后返回
        return self.quick_sort_random(left) + mid + self.quick_sort_random(right)

    #     三数取中法
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
        povit = self.median_of_three(arr)
        # 同上
        left = [x for x in arr if x < povit]
        right = [x for x in arr if x > povit]
        mid = [x for x in arr if x == povit]
        return self.quick_sort_median(left) + mid + self.quick_sort_median(right)


# 原地排序实现（节省空间）
#     def partition(self,arr,low,high):


arr = [10, 7, 8, 9, 1, 5]
# print(QuickSort().quick_sort_random(arr))
print(QuickSort().quick_sort_median(arr))
