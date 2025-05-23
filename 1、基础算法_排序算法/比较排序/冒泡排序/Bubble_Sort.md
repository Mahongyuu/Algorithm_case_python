冒泡排序 (Bubble Sort)
核心思想
冒泡排序是一种简单的交换排序算法，其核心思想是通过相邻元素的比较和交换，将较大的元素逐步“冒泡”到数组的末尾（或较小的元素“冒泡”到数组开头）。每一轮排序会将当前未排序部分的最大（或最小）元素放到正确的位置。

算法步骤
比较相邻元素：从数组的第一个元素开始，依次比较相邻的两个元素。

交换顺序：如果前一个元素比后一个元素大（升序排序），则交换它们的位置。

重复遍历：对数组进行多轮遍历，每一轮都会将当前未排序部分的最大元素“冒泡”到最后。

终止条件：当某一轮遍历中没有发生任何交换时，说明数组已经有序，排序结束。

算法案例
示例数组：[5, 3, 8, 4, 2]
升序排序过程：

第一轮：

比较 5 和 3 → 交换 → [3, 5, 8, 4, 2]

比较 5 和 8 → 不交换

比较 8 和 4 → 交换 → [3, 5, 4, 8, 2]

比较 8 和 2 → 交换 → [3, 5, 4, 2, 8]
（最大元素 8 已到末尾）

第二轮：

比较 3 和 5 → 不交换

比较 5 和 4 → 交换 → [3, 4, 5, 2, 8]

比较 5 和 2 → 交换 → [3, 4, 2, 5, 8]
（次大元素 5 已到正确位置）

第三轮：

比较 3 和 4 → 不交换

比较 4 和 2 → 交换 → [3, 2, 4, 5, 8]
（元素 4 已到正确位置）

第四轮：

比较 3 和 2 → 交换 → [2, 3, 4, 5, 8]
（元素 3 已到正确位置）

第五轮：无交换，排序完成。

复杂度分析
时间复杂度：

最坏情况（逆序数组）：需进行 n(n−1)/2 次比较和交换，为 O(n^2)。

最好情况（已有序数组）：仅需一轮遍历，为 O(n)。

平均情况： O(n^2)。

空间复杂度：仅需常数额外空间（原地排序），为 O(1)。

稳定性：是稳定排序（相等元素不交换）。

Python 代码实现
def bubble_sort(arr):
n = len(arr)
for i in range(n):
swapped = False  # 优化：标记本轮是否发生交换
for j in range(0, n - i - 1):
if arr[j] > arr[j + 1]:
arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换
swapped = True
if not swapped:  # 若无交换，提前结束
break
return arr

# 测试
arr = [5, 3, 8, 4, 2]
print("排序前:", arr)
sorted_arr = bubble_sort(arr)
print("排序后:", sorted_arr)
输出：

排序前: [5, 3, 8, 4, 2]
排序后: [2, 3, 4, 5, 8]
关键点总结
优化：通过 swapped 标志可提前终止排序（若数组已有序）。

适用场景：小规模数据或教学示例，实际应用中效率较低。