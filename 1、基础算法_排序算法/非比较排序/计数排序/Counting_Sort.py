import time


class CountingSort:

    def counting_sort(self, arr):
        """
            计数排序：类记牌器逻辑，先统计元素范围，再将元素出现的次数统计，再组合。
            :param arr: 待排序数组（假设元素为非负整数）
            :return: 排序后的数组
        """
        if not arr:  # 边界条件
            return arr

        max_val = max(arr)
        min_val = min(arr)  # 取最大值和最小值
        # 计算'计数'数组的长度
        count_size = max_val - min_val + 1
        count = [0] * count_size  # 创建'计数'数组
        # 统计每个数出现的频次(次数)
        for num in arr:
            count[num - min_val] += 1
        # 计算前缀和（确定每个元素的最终位置）
        for i in range(1, count_size):
            count[i] += count[i - 1]
        # 从后向前遍历原数组，放置元素到结果数组
        sorted_arr = [0] * len(arr)
        for num in reversed(arr):  # 采用反向遍历以确保稳定
            pos = count[num - min_val] - 1  # 计算每个数应该放的正确位置
            sorted_arr[pos] = num
            count[num - min_val] -= 1  # 更新前缀和

        return sorted_arr

    def counting_sort_simple(self, arr):
        max_val = max(arr)  # 取最大值
        count_arr = [0] * (max_val + 1)  # 依据最大值+1为长度给出'计数'数组
        # 遍历待排序的数组,将每个元素作为计数数组的下标,出现一次,计数(记录)一次
        for num in arr:
            count_arr[num] += 1
        sorted_simple_arr = []
        # 关键字enumerate() 将元素和索引一起遍历
        for i, count in enumerate(count_arr):
            if count != 0:
                # 根据计数数组的下标和下标对应的值(元素出现的次数)组成排序后的数组
                sorted_simple_arr += [i] * count
        return sorted_simple_arr


# # 测试示例
if __name__ == "__main__":

    arr = [90, 889, 935, 986, 585, 431, 356, 905, 736, 390, 530, 137, 970, 134, 630, 14, 976, 577, 147, 930, 585, 302, 598, 407, 950, 186, 958, 811, 956, 752, 667, 935, 48, 25, 413, 929, 729, 666, 708, 123, 317, 919, 956, 12, 692, 802, 357, 478, 496, 563, 226, 483, 271, 229, 923, 177, 122, 704, 197, 758, 181, 524, 955, 128, 400, 679, 588, 861, 699, 874, 684, 198, 827, 858, 385, 199, 209, 773, 675, 703, 186, 261, 583, 691, 496, 378, 639, 426, 446, 617, 826, 147, 754, 476, 376, 855, 971, 932, 388, 967]
    print("排序前数组1:\n", arr)
    start = time.perf_counter()
    sorted_arr = CountingSort().counting_sort(arr)
    end = time.perf_counter()
    print("排序后数组1:\n", sorted_arr)
    print('排序数组1用时：', end - start)

    # 使用enumerate函数组合排序
    arr_1 = [436, 246, 85, 374, 187, 360, 552, 216, 400, 985, 297, 339, 723, 581, 364, 612, 975, 270, 717, 120, 55, 670, 838, 640, 366, 804, 984, 469, 47, 277, 717, 735, 206, 930, 416, 86, 189, 71, 181, 236, 386, 257, 697, 749, 319, 541, 621, 886, 909, 969, 875, 330, 903, 404, 5, 655, 498, 740, 757, 452, 983, 285, 504, 405, 878, 963, 411, 529, 823, 974, 73, 444, 898, 960, 8, 81, 260, 687, 649, 26, 341, 104, 254, 679, 879, 380, 931, 272, 639, 215, 108, 629, 394, 720, 632, 336, 607, 977, 426, 423]
    print("排序前数组2:\n", arr_1)
    start_1 = time.perf_counter()
    sorted_arr_simple = CountingSort().counting_sort_simple(arr_1)
    end_1 = time.perf_counter()
    print('排序后数组2:\n', sorted_arr_simple)
    print('排序数组1用时：', end_1 - start_1)
