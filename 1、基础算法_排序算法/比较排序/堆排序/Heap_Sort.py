# class HeapSort:
#     def heapify(self, arr, n, i):
#         largest = i
#         left = i * 2 + 1
#         right = i * 2 + 2
#         if left < n and arr[left] > arr[right]:
#             largest = left
#         if right < n and arr[right] > arr[left]:
#             largest = right
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             self.heapify(arr, n, 0)
#
#     def heap_sort(self, arr):
#         n = len(arr)
#         for i in range(n // 2 - 1, -1, -1):
#             self.heapify(arr, n, i)
#         for i in range(n - 1, 0, -1):
#             arr[0], arr[i] = arr[i], arr[0]
#             self.heapify(arr, n, i)
#
#
# arr = [12, 11, 13, 5, 6, 7]
# print(HeapSort().heapify(arr,n,i))
class HeapSort:
    def heapify(self, arr, n, i):
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


# 测试
arr = [12, 11, 13, 5, 6, 7]
HeapSort().heap_sort(arr)
print("排序结果:", arr)  # 输出: [5, 6, 7, 11, 12, 13]