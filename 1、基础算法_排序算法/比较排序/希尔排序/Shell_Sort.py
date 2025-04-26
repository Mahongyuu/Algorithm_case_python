import time


class Shellsort:

    def shell_sort(self, arr):
        """
        希尔排序：通过gap来均等逐步拆分数据逐步插入排序
        :param arr: 排序前的数组
        :return: 排序后的数组
        """
        # 取数组长度
        n = len(arr)
        gap = n // 2  # gap拆分逻辑
        # 对拆分后的子序列排序
        while gap > 0:
            # 此处的range范围里的arr[i]和插入排序处的arr[j-gap]即组成被gap拆分后的一对子序列
            for i in range(gap, n):
                temp = arr[i]  # 类插入中的key
                j = i
                # 插入排序逻辑
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2  # gap再拆分逻辑
        return arr


start = time.perf_counter()

if __name__ == '__main__':
    arr = [444, 844, 30, 218, 977, 620, 760, 193, 113, 447, 367, 590, 63, 891, 816, 352, 182, 933, 800, 912, 788, 430, 646, 143, 900, 989, 72, 162, 712, 941, 510, 324, 900, 128, 871, 317, 322, 757, 806, 453, 262, 736, 192, 252, 915, 327, 103, 597, 701, 13, 665, 976, 78, 1, 276, 427, 877, 806, 803, 83, 876, 238, 648, 939, 894, 444, 57, 929, 633, 705, 141, 202, 163, 754, 886, 736, 274, 787, 529, 904, 723, 191, 803, 216, 996, 750, 546, 81, 744, 410, 277, 641, 651, 521, 396, 77, 418, 13, 191, 179]
    print('排序前的数组为：\n', arr)
    sorted_arr = Shellsort().shell_sort(arr)
    print('排序后的数组为：\n', sorted_arr)

end = time.perf_counter()
print('程序运行时间为：', end - start)
