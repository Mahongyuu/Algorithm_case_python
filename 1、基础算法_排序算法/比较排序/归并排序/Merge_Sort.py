import time


class Solution:

    def merge_sort(self, arr):
        """
        归并排序：
        :param arr:
        :return:
        """
        # 边界条件
        if len(arr) <= 1:
            return arr
        # 取中位值
        mid = len(arr) // 2
        # 左分区迭代
        left = self.merge_sort(arr[:mid])
        # 右分区迭代
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        # 初始化
        result = []
        i, j = 0, 0
        # 定义双指针来比对值
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # 偏小值往左添加
                result.append(left[i])
                i += 1
            else:
                # 偏大值往右边添加
                result.append(right[j])
                j += 1
                # 用extend（）拼接
                # ‘extend（）’可以拼接可迭代对象，如列表、元组、字符串等
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # 非递归实现（自底向上）
    def merge_sort_iterative(self, arr):
        n = len(arr)
        size = 1  # 初始子数组大小为1
        while size < n:
            for start in range(0, n, 2 * size):  # 按步长遍历
                mid = min(start + size, n)  # 中间点
                end = min(start + 2 * size, n)  # 子数组结束点
                merged = self.merge(arr[start:mid], arr[mid:end])  # 合并两个子数组
                arr[start:end] = merged  # 将合并结果写回原数组
            size *= 2  # 子数组大小翻倍
        return arr


if __name__ == '__main__':

    arr = [676, 856, 390, 701, 306, 951, 967, 397, 856, 959, 340, 89, 896, 851, 486, 509, 446, 553, 590, 309, 802, 360, 521, 557, 738, 95, 944, 871, 934, 17, 384, 172, 521, 847, 165, 847, 706, 225, 701, 288, 925, 789, 634, 586, 688, 465, 899, 948, 514, 241, 898, 929, 552, 445, 602, 92, 177, 592, 106, 578, 191, 773, 65, 486, 810, 997, 36, 205, 82, 239, 235, 990, 648, 226, 535, 782, 412, 52, 478, 743, 535, 966, 700, 34, 523, 11, 785, 311, 217, 919, 846, 86, 130, 499, 976, 558, 448, 138, 639, 848]
    print('排序前的数组1：\n', arr)
    start = time.perf_counter()
    sorted_arr = Solution().merge_sort(arr)
    end = time.perf_counter()
    print('排序后的数组1：\n', sorted_arr)
    print('排序数组1用时：', end - start)

    arr0 = [323, 59, 736, 309, 634, 355, 560, 287, 737, 958, 976, 599, 3, 232, 413, 53, 919, 316, 952, 430, 226, 979, 756, 817, 119, 514, 344, 492, 937, 681, 249, 441, 221, 998, 611, 667, 957, 844, 373, 684, 130, 857, 603, 906, 905, 348, 480, 591, 46, 24, 856, 73, 53, 23, 52, 889, 385, 269, 754, 967, 770, 320, 78, 294, 825, 249, 497, 554, 474, 374, 51, 315, 371, 707, 337, 48, 28, 919, 397, 400, 546, 482, 789, 69, 995, 261, 961, 44, 833, 769, 150, 598, 474, 898, 974, 775, 884, 261, 606, 575]
    print('排序前的数组2：\n', arr0)
    start_0 = time.perf_counter()
    sorted_arr0 = Solution().merge_sort_iterative(arr0)
    end_0 = time.perf_counter()
    print('排序后的数组2：\n', sorted_arr0)
    print('排序数组2用时：', end_0 - start_0)


