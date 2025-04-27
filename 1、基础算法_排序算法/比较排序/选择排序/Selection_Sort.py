import time


class SelectionSort:

    def selection_sort(self, arr):
        """
        选择排序：通过确定一个元素比较出最小值或最大值，
        然后将最小或最大值放置在最前面或最后面完成排序。
        :param arr: 需要排序的数组
        :return: 排序后的数组
        """
        # 取数组长度
        n = len(arr)
        for i in range(n):
            min_idx = i  # 假设当前元素（arr[i]）为最小
            for j in range(i + 1, n):  # 在未排序的部分寻找比arr[i]小的值
                if arr[j] < arr[min_idx]:
                    min_idx = j  # 重新假设最小值
                arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 元素交换
        return arr

    def selection_sort_optimized(self, arr):
        """
        优化版本；同时找最小值和最大值
        :param arr:
        :return:
        """
        n = len(arr)
        for i in range(n // 2):
            min_idx, max_idx = i, i
            for j in range(i, n - i):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if max_idx == i:
                max_idx = min_idx
            arr[n - i - 1], arr[max_idx] = arr[max_idx], arr[n - i - 1]
        return arr



if __name__ == '__main__':
    arr = [239, 123, 686, 695, 528, 95, 837, 666, 920, 810, 182, 771, 705, 290, 171, 65, 760, 520, 567, 484, 436, 329, 885, 864, 623, 742, 57, 471, 970, 402, 796, 739, 866, 858, 237, 796, 398, 518, 704, 272, 161, 913, 905, 883, 849, 857, 660, 650, 596, 26, 493, 404, 230, 874, 16, 780, 536, 253, 333, 111, 852, 877, 707, 619, 421, 879, 452, 932, 225, 930, 227, 828, 222, 6, 64, 421, 451, 911, 300, 842, 927, 206, 340, 406, 187, 779, 982, 96, 701, 263, 834, 400, 682, 238, 393, 859, 571, 79, 961, 416]
    print('排序前数组1为：\n', arr)
    start = time.perf_counter()
    sorted_arr = SelectionSort().selection_sort(arr)
    end = time.perf_counter()
    print('排序后数组1为：\n', sorted_arr)
    print('排序数组1所用时间为：', end - start)

    arr_1 = [611, 819, 486, 938, 697, 468, 73, 857, 361, 384, 387, 42, 794, 346, 235, 938, 944, 123, 290, 235, 341, 714, 644, 977, 824, 874, 948, 625, 392, 260, 343, 939, 748, 937, 818, 817, 7, 251, 915, 882, 258, 892, 290, 224, 781, 813, 635, 980, 463, 493, 299, 197, 563, 447, 124, 386, 876, 96, 838, 46, 751, 772, 631, 715, 616, 929, 510, 898, 859, 200, 42, 383, 68, 368, 520, 876, 949, 219, 767, 632, 111, 810, 230, 456, 651, 993, 861, 479, 912, 77, 900, 110, 989, 82, 674, 569, 98, 890, 269, 384]
    print('排序前数组1为：\n', arr_1)
    start_1 = time.perf_counter()
    sorted_arr_1 = SelectionSort().selection_sort_optimized(arr_1)
    end_1 = time.perf_counter()
    print('排序后数组2为：\n', sorted_arr_1)
    print('排序数组2所用时间为：', end_1 - start_1)
