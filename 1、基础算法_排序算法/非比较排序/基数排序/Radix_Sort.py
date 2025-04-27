import time


class RadixSort:

    def radix_sort(self, arr):
        """
        基数排序：即取数组中最大值按位分配（0-9）10个桶然后桶内排序
        例如：369 即3位数，分配个位10个桶，十位10个，百位10个
        :param arr: 需要排序的数组
        :return: 排序后的数组
        """
        max_val = max(arr)  # 找到最大值
        max_digit = len(str(max_val))  # 取最大值的位数长度

        for i in range(max_digit):
            # 创建第i次的10个桶
            buckets = [[] for _ in range(10)]
            # 按位数将元素分配到桶
            for num in arr:
                # 取元素位数（第i次为i位）
                current_digit = (num // (10 ** i)) % 10
                buckets[current_digit].append(num)
            # 列表推导（将二维列表转换为一维列表）且收集桶内数据
            arr = [num for bucket in buckets for num in bucket]
        return arr

    def msd_radix_sort(self, arr, digit=None):
        """
        通过递归实现基数排序
        :param arr: 需要排序的数组
        :param digit: 位次
        :return: 排序后的数组
        """
        if digit is None:
            max_val = max(arr)
            digit = len(str(max_val)) - 1

        if digit < 0 or len(arr) <= 1:
            return arr

        buckets = [[] for _ in range(10)]
        for num in arr:
            current_digit = (num // (10 ** digit)) % 10
            buckets[current_digit].append(num)
        # 桶内递归进行排序
        sorted_buckets = []
        for bucket in buckets:
            if bucket:
                sorted_buckets.extend(RadixSort().msd_radix_sort(bucket, digit - 1))
        return sorted_buckets


if __name__ == '__main__':
    arr = [530, 478, 986, 398, 829, 518, 469, 371, 536, 482, 19, 921, 899, 817, 545, 469, 963, 736, 471, 606, 771, 266, 42, 730, 145, 112, 927, 670, 910, 28, 302, 579, 838, 221, 304, 301, 321, 563, 180, 145, 268, 417, 450, 16, 110, 36, 310, 942, 68, 32, 560, 121, 655, 178, 294, 929, 648, 380, 614, 802, 397, 781, 879, 517, 177, 387, 670, 790, 284, 202, 487, 849, 81, 485, 768, 404, 289, 509, 108, 854, 725, 456, 264, 376, 122, 856, 275, 59, 275, 533, 179, 275, 228, 566, 475, 376, 399, 922, 481, 317]
    print('排序前数组1为：\n', arr)
    start = time.perf_counter()
    sorted_arr = RadixSort().radix_sort(arr)
    end = time.perf_counter()
    print('排序后数组1为：\n', sorted_arr)
    print('排序数组1所用时间为：', end - start)

    arr_1 = [264, 116, 74, 275, 375, 829, 862, 94, 576, 351, 397, 626, 252, 161, 166, 638, 161, 246, 1, 946, 884, 907, 538, 995, 761, 285, 543, 915, 618, 876, 6, 152, 28, 606, 716, 487, 629, 756, 551, 722, 674, 963, 881, 476, 139, 703, 458, 576, 628, 840, 504, 998, 337, 978, 691, 210, 194, 971, 5, 331, 487, 271, 563, 691, 398, 673, 723, 535, 908, 22, 636, 45, 34, 550, 21, 838, 828, 252, 677, 614, 639, 388, 36, 938, 76, 916, 231, 834, 103, 356, 963, 420, 308, 7, 985, 252, 879, 234, 771, 908]
    print('排序前数组1为：\n', arr_1)
    start_1 = time.perf_counter()
    sorted_arr_1 = RadixSort().msd_radix_sort(arr_1)
    end_1 = time.perf_counter()
    print('排序后数组2为：\n', sorted_arr_1)
    print('排序数组2所用时间为：', end_1 - start_1)
