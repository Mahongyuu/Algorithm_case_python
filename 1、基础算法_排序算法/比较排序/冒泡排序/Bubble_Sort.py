import time


class BubbleSort:
    def bubble_sort(self, arr):
        """
        :param arr:需要排序的数组
        :return: 排序后的数组
        """
        # 获取数组长度
        n = len(arr)
        for i in range(n):
            # swapped用于标记本轮是否进行了交换
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:  # 元素比较
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 元素交换
                    swapped = True  # 标记
            if not swapped:  # 边界
                break
        return arr


start = time.perf_counter()  # 高精度计时

# 你的代码
if __name__ == '__main__':
    arr = [344, 500, 807, 986, 418, 942, 298, 680, 532, 142, 830, 57, 393, 330, 354, 217, 587, 429, 360, 972, 968, 621,
           182, 673, 98, 79, 319, 239, 243, 724, 261, 338, 324, 738, 99, 986, 296, 629, 73, 218, 824, 901, 963, 560,
           884, 137, 547, 93, 511, 168, 721, 398, 259, 597, 551, 189, 611, 799, 668, 767, 196, 864, 344, 650, 25, 392,
           749, 324, 453, 678, 334, 385, 850, 524, 953, 889, 262, 715, 501, 767, 599, 680, 351, 132, 189, 757, 595, 36,
           881, 729, 970, 402, 232, 746, 852, 195, 853, 576, 670, 445]
    print('排序前数组为：\n', arr)
    sorted_arr = BubbleSort().bubble_sort(arr)
    print('排序后数组为：\n', sorted_arr)

end = time.perf_counter()
print(f"程序运行时间：{end - start} 秒")
