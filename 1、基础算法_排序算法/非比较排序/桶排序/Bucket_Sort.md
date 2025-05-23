桶排序（Bucket Sort）

核心思想
桶排序是一种分布式排序算法，适用于数据分布均匀且范围已知的情况。其核心思想是：

分桶：将数据分配到有限数量的“桶”中，每个桶内的数据范围固定。

桶内排序：对每个桶内的数据单独排序（通常使用插入排序等简单算法）。

合并结果：按桶的顺序依次输出所有数据，得到有序序列。

算法步骤
确定桶的数量和范围：

根据数据范围和分布特性，划分若干个区间（桶）。

例如，数据范围 [0, 100) 可分为 10 个桶，每个桶范围 [0, 10), [10, 20), ..., [90, 100)。

分配数据到桶中：
遍历数组，将每个元素放入对应的桶。

对每个桶排序：
使用任意排序算法（如插入排序、快速排序）对每个桶内数据排序。

合并桶的结果：
按桶的顺序依次输出所有元素，得到全局有序序列。

算法案例
输入数组：[29, 25, 3, 49, 9, 37, 21, 43]
数据范围：0 ≤ x < 50
分桶规则：划分为 5 个桶，每个桶范围 [0, 10), [10, 20), ..., [40, 50)。

分桶：
桶 0 ([0, 10)): [3, 9]
桶 1 ([10, 20)): [21]
桶 2 ([20, 30)): [29, 25]
桶 3 ([30, 40)): [37]
桶 4 ([40, 50)): [49, 43]

桶内排序：
桶 0: [3, 9]（已有序）
桶 1: [21]（无需排序）
桶 2: [25, 29]
桶 3: [37]
桶 4: [43, 49]

合并结果：
输出顺序：[3, 9, 21, 25, 29, 37, 43, 49]

复杂度分析
时间复杂度：

最佳情况（数据均匀分布）：O(n + k)，其中 n 是元素数量，k 是桶数量。

分配数据到桶：O(n)。

桶内排序：若每个桶内数据量接近 n/k，且使用 O(m log m) 的排序算法，总时间为 k * O((n/k) log(n/k)) ≈ O(n log(n/k))。

合并结果：O(n)。

最坏情况（所有数据集中在一个桶）：退化为 O(n²)（如桶内用插入排序）。

空间复杂度

O(n + k)，需要额外空间存储桶和桶内数据。

稳定性：
桶排序可以是稳定的，取决于桶内排序算法的稳定性（如插入排序是稳定的）。

适用场景
数据分布均匀：能保证元素均匀分散到各个桶中。

范围已知：需要提前知道数据的上下界。

外部排序：适合处理大数据量且内存受限的场景（如分布式系统）。

Python 代码实现
def bucket_sort(arr, bucket_size=10):
    if len(arr) == 0:
        return arr

    # 1. 确定数据范围
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # 2. 分配数据到桶中
    for num in arr:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)

    # 3. 对每个桶排序（这里用内置排序，实际可用插入排序）
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # 使用 Timsort (O(n log n))

    return sorted_arr

# 测试
arr = [29, 25, 3, 49, 9, 37, 21, 43]
print(bucket_sort(arr))  # 输出: [3, 9, 21, 25, 29, 37, 43, 49]