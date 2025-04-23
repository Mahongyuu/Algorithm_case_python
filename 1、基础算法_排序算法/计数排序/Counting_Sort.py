class CountingSort:
    def counting_sort(self, arr):
        """
        #     计数排序算法实现
        #     :param arr: 待排序数组（假设元素为非负整数）
        #     :return: 排序后的数组
        #     """
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
    arr = [7, 5, 3, 3, 1, 3, 6, 9]
    arr_1 = [4, 2, 2, 8, 3, 3, 1]
    print("原始数组1:", arr)
    print("原始数组2:", arr_1)
    sorted_arr = CountingSort().counting_sort(arr)
    print("排序结果:", sorted_arr)
    sorted_arr_simple = CountingSort().counting_sort_simple(arr_1)
    print('使用enumerate函数组合排序:', sorted_arr_simple)
