import time


class HeapSort:

    def heapify(self, arr, n, i):
        """
        堆排序：
        :param arr:
        :param n:
        :param i:
        :return:
        """
        largest = i  # 当前父节点
        left = 2 * i + 1  # 左子节点
        right = 2 * i + 2  # 右子节点

        # 比较左子节点和父节点
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 比较右子节点和当前最大值
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 如果最大值不是父节点，交换并继续调整
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)  # 递归调整被交换的子节点

    def heap_sort(self, arr):
        n = len(arr)

        # 1. 构建最大堆（从最后一个非叶子节点开始）
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # 2. 逐个提取堆顶元素（最大值）到数组末尾
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # 交换堆顶和末尾元素
            self.heapify(arr, i, 0)  # 调整剩余堆（大小变为i）
        return arr


start = time.perf_counter()
# 测试
if __name__ == '__main__':
    arr = [967, 650, 65, 757, 930, 539, 114, 724, 693, 241, 365, 74, 878, 572, 328, 182, 895, 774, 229, 407, 761, 9, 387, 326, 308, 49, 853, 515, 598, 955, 29, 202, 436, 972, 45, 393, 915, 844, 57, 350, 84, 324, 407, 273, 782, 504, 74, 501, 898, 489, 879, 282, 715, 634, 412, 555, 265, 443, 216, 463, 405, 239, 802, 363, 295, 853, 251, 768, 975, 436, 149, 463, 800, 508, 615, 724, 494, 322, 770, 864, 209, 594, 364, 429, 500, 572, 28, 870, 78, 870, 337, 157, 801, 892, 394, 319, 894, 615, 492, 549]
    print('排序前的数组为：\n', arr)
    sorted_arr = HeapSort().heap_sort(arr)
    print('排序后的数组为：\n', sorted_arr)
end = time.perf_counter()
print('此程序运行时间为：', end - start)