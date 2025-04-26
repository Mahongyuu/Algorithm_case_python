import random
import time


class QuickSort:
    # 一、随机取值
    def quick_sort_random(self, arr):
        """
        快速排序：
        :param arr:
        :return:
        """
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
if __name__ == '__main__':
    # 测试一、随机取值
    arr1 = [196, 868, 577, 673, 719, 955, 919, 744, 322, 199, 36, 215, 552, 425, 596, 199, 994, 812, 858, 135, 131, 535, 997, 489, 425, 243, 267, 445, 588, 177, 491, 502, 113, 306, 772, 103, 477, 932, 358, 468, 471, 792, 289, 874, 562, 348, 525, 396, 243, 578, 322, 163, 714, 475, 574, 920, 157, 976, 842, 188, 543, 187, 437, 615, 110, 458, 790, 866, 748, 919, 813, 418, 246, 135, 381, 485, 277, 344, 278, 712, 99, 428, 161, 673, 241, 432, 767, 527, 110, 301, 847, 917, 754, 744, 24, 789, 784, 703, 277, 556]
    print('排序前数组1为：\n', arr1)
    start1 = time.perf_counter()
    sorted_arr1 = QuickSort().quick_sort_random(arr1)
    end1 = time.perf_counter()
    print('排序后数组1为：\n', sorted_arr1)
    print('排序数组1用时：', end1 - start1)

    # 测试二、三数取中法
    arr2 = [606, 733, 58, 936, 880, 716, 789, 295, 389, 202, 49, 453, 598, 754, 619, 180, 139, 885, 641, 438, 603, 321, 15, 251, 364, 232, 563, 116, 986, 505, 92, 540, 258, 274, 478, 3, 244, 158, 651, 946, 148, 230, 316, 676, 710, 159, 630, 238, 589, 39, 713, 937, 742, 708, 550, 215, 383, 201, 161, 651, 961, 298, 744, 12, 252, 935, 880, 368, 289, 38, 585, 391, 735, 487, 360, 481, 947, 460, 281, 105, 470, 843, 212, 306, 527, 299, 683, 473, 34, 652, 512, 492, 839, 733, 909, 58, 91, 215, 727, 584]
    print('排序前数组1为：\n', arr2)
    start2 = time.perf_counter()
    sorted_arr2 = QuickSort().quick_sort_median(arr2)
    end2 = time.perf_counter()
    print('排序后数组1为：\n', sorted_arr2)
    print('排序数组1用时：', end2 - start2)

    # 测试三、原地排序实现
    arr3 = [908, 683, 306, 170, 762, 917, 876, 715, 706, 704, 109, 537, 240, 422, 443, 560, 544, 813, 245, 602, 388, 807, 856, 919, 249, 992, 27, 174, 310, 852, 891, 931, 165, 333, 227, 24, 94, 571, 148, 492, 698, 65, 279, 534, 330, 161, 613, 542, 443, 908, 767, 832, 865, 161, 814, 837, 421, 983, 408, 241, 175, 390, 671, 284, 520, 952, 778, 835, 622, 281, 26, 157, 634, 54, 330, 74, 111, 414, 846, 139, 906, 949, 72, 900, 612, 571, 423, 81, 294, 392, 856, 375, 167, 175, 321, 118, 951, 35, 43, 284]
    print('排序前数组1为：\n', arr3)
    start3 = time.perf_counter()
    sorted_arr3 = QuickSort().quick_sort_inplace(arr3)
    end3 = time.perf_counter()
    print('排序后数组1为：\n', sorted_arr3)
    print('排序数组1用时：', end3 - start3)