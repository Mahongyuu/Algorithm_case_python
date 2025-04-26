基数排序 (Radix Sort)
核心思想
基数排序是一种 非比较型整数排序算法，其核心思想是：

按数字的每一位（从低位到高位或高位到低位）进行分组排序（通常使用 计数排序 或 桶排序 作为子排序算法）。

逐位排序：通过多次分配和收集，逐步使整个数组有序。

关键点
适用于整数或字符串（如电话号码、日期等固定长度的数据）。

稳定性依赖子排序算法（如使用稳定的计数排序）。

算法步骤
确定最大数字的位数（max_digit）：决定需要排序的轮次。

从最低位（LSD）到最高位（MSD）（或反向）逐位排序：

分配：根据当前位的值（0~9），将元素分配到对应的桶（buckets）。

收集：按桶的顺序（0→9）合并回原数组。

重复：直到所有位处理完毕，数组有序。

两种实现方式
LSD（Least Significant Digit）：从最低位开始（更常用）。

MSD（Most Significant Digit）：从最高位开始（类似字典序，需递归）。

算法案例
示例数组：[170, 45, 75, 90, 802, 24, 2, 66]
步骤（LSD 方式）：

第1轮（个位）：

分配到桶：

0: [90]
2: [802, 2]
4: [24]
5: [45, 75]
6: [66]
7: [170]
收集结果：[90, 802, 2, 24, 45, 75, 66, 170]

第2轮（十位）：

分配到桶：

0: [802, 2]
2: [24]
4: [45]
6: [66]
7: [170, 75]
9: [90]
收集结果：[802, 2, 24, 45, 66, 170, 75, 90]

第3轮（百位）：

分配到桶：

0: [2, 24, 45, 66, 75, 90]
1: [170]
8: [802]
收集结果：[2, 24, 45, 66, 75, 90, 170, 802]

复杂度分析
情况	    时间复杂度	空间复杂度	稳定性
最坏情况 O(d⋅(n+k))   O(n+k)	    稳定
平均情况 O(d⋅(n+k))   O(n+k)	    稳定
最好情况 O(d⋅(n+k))   O(n+k)	    稳定

变量说明：

n：数组长度。

k：基数（十进制时为 10）。

d：最大数字的位数。

特点：

稳定排序（若子排序稳定）。

不适合非整数数据（需转换为整数形式，如浮点数需特殊处理）。

Python 代码实现
LSD 基数排序（基于计数排序）
def radix_sort(arr):
    max_num = max(arr)  # 找到最大值确定位数
    max_digit = len(str(max_num))  # 最大位数
    
    for digit in range(max_digit):
        # 10个桶（0~9）
        buckets = [[] for _ in range(10)]
        # 按当前位分配到桶
        for num in arr:
            current_digit = (num // (10 ** digit)) % 10
            buckets[current_digit].append(num)
        # 收集桶中的数据
        arr = [num for bucket in buckets for num in bucket]
    return arr

# 测试
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("排序前:", arr)
sorted_arr = radix_sort(arr.copy())
print("排序后:", sorted_arr)
输出：

排序前: [170, 45, 75, 90, 802, 24, 2, 66]
排序后: [2, 24, 45, 66, 75, 90, 170, 802]

MSD 基数排序（递归实现）
def msd_radix_sort(arr, digit=None):
    if digit is None:
        max_num = max(arr)
        digit = len(str(max_num)) - 1  # 从最高位开始
    
    if digit < 0 or len(arr) <= 1:
        return arr
    
    buckets = [[] for _ in range(10)]
    for num in arr:
        current_digit = (num // (10 ** digit)) % 10
        buckets[current_digit].append(num)
    
    # 递归处理每个桶的下一位
    sorted_buckets = []
    for bucket in buckets:
        if bucket:
            sorted_buckets.extend(msd_radix_sort(bucket, digit - 1))
    
    return sorted_buckets

适用场景
固定长度的整数或字符串（如身份证号、电话号码）。

数据范围已知且位数较小（如 d 远小于 n）。

需要稳定排序且避免比较操作。

基数排序在特定场景下比快速排序更高效，但通用性较低！