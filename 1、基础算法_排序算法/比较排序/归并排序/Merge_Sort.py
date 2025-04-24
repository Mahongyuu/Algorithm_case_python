class Solution:
    def merge_sort(self, arr):
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
    def merge_sort_iterative(self,arr):
        n = len(arr)
        size = 1  # 初始子数组大小为1
        while size < n:
            for start in range(0, n, 2 * size):  # 按步长遍历
                mid = min(start + size, n)        # 中间点
                end = min(start + 2 * size, n)    # 子数组结束点
                merged = self.merge(arr[start:mid], arr[mid:end])  # 合并两个子数组
                arr[start:end] = merged           # 将合并结果写回原数组
            size *= 2  # 子数组大小翻倍
        return arr


arr = [38, 27, 43, 3, 9, 82, 10]
arr0 = [15, 456, 45, 78, 8, 94, 76]
sorted_arr0 = Solution().merge_sort_iterative(arr0)
sorted_arr = Solution().merge_sort(arr)
print("排序后:", sorted_arr)
print("排序后:", sorted_arr0)
