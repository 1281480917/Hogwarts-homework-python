'''
1. 时间复杂度问题
已知 AList = [1, 2, 3]，BSet = {1, 2, 3} (1)从AList和BSet中查找4，最坏时间复杂度哪个大？(2)从AList和BSet中插入4，最坏时间复杂度哪个大？

答:

对于查找，列表和集合的最坏时间复杂度都是O(n)，所以一样的。
列表操作插入的最坏时间复杂度为o(n), 集合为o(1)，所以Alist大。set是哈希表所以操作的复杂度基本上都是o(1)。
'''
def binary_search(arr,target):
    '''
     用 Python 实现一个二分查找的函数
    https://www.cnblogs.com/kyoner/p/11080078.html
    :param arr:有序列表
    :param target:要查找的数
    :return:
    '''
    n=len(arr)
    left=0
    right=n-1
    while left<=right:#搜索区间为空的时候应该终止
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            left=mid+1 #[mid + 1, right]
        elif arr[mid]>target:
            right=mid-1 #[left, mid - 1]
    return -1


if __name__ == '__main__':
    l = [1, 3, 4, 5, 6, 7, 8]
    print(binary_search(l, 6))
class Book:
    '''
    Python 单例模式的实现方法
    一个对象的实例化过程是先执行类的__new__方法,如果我们没有写,默认会调用object的__new__方法,
    返回一个实例化对象,然后再调用__init__方法,
    对这个对象进行初始化,我们可以根据这个实现单例.
    在一个类的__new__方法中先判断是不是存在实例,如果存在实例,就直接返回,如果不存在实例就创建.
    '''
    def __new__(cls, title):
        if not hasattr(cls, "_ins"):
            cls._ins = super().__new__(cls)
            print('in __new__')

        return cls._ins

    def __init__(self, title):
        print('in __init__')
        super().__init__()
        self.title = title

if __name__ == '__main__':
    b = Book('The Spider Book')
    b2 = Book('The Flask Book')
    print(id(b))
    print(id(b2))
    print(b.title)
    print(b2.title)


def fibonacci(num):
    '''
    斐波那契数列
    有个人想知道，一年之内一对兔子能繁殖多少对？于是就筑了一道围墙把一对兔子关在里面。
    已知一对兔子每个月可以生一对小兔子，而一对兔子从出生后第3个月起每月生一对小兔子。
    假如一年内没有发生死亡现象，那么，一对兔子一年内（12个月）能繁殖成多少
    F0 = 0 (n=0)
    F1 = 1 (n=1)
    Fn = F[n-1]+ F[n-2](n=>2)
    :param num:
    :return:
    '''
    if num==1 or num==2:
       return 1
    return fibonacci(num-1)+fibonacci(num-2)

if __name__ == '__main__':
    print(fibonacci(3))

def bubble_sort(arr):
    '''
    冒泡排序：把相邻的元素两两进行比较，根据大小交换元素的位置
    :param arr:
    :return:
    '''
    n = len(arr)
    for i in range(n - 1):
        #控制所有回合，轮转的次数和元素数量相当
        for j in range(n - i - 1):
            #每一轮的冒泡处理，每一轮都能确定一个数最终位置，所以要n-i
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
    bubble_sort(l)
    print(l)

def quick_sort(lists,i,j):
    '''
     快速排序：
      http://www.ruanyifeng.com/blog/2011/04/quicksort_in_javascript.html?bsh2%E3%80%81_bid=124324679
     （1）在数据集之中，选择一个元素作为"基准"（pivot）。
 　　（2）所有小于"基准"的元素，都移到"基准"的左边；所有大于"基准"的元素，都移到"基准"的右边。
 　　（3）对"基准"左边和右边的两个子集，不断重复第一步和第二步，直到所有子集只剩下一个元素为止
     :param arr:
     :param first:
     :param last:
     :return:
     '''
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists, low, i - 1)
    quick_sort(lists, i + 1, high)
    return lists

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
    quick_sort(l,0,len(l)-1)
    print(l)









#4. 使用 Python 实现一个斐波那契数列
#5. 找出列表中的重复数字
#6. 找出列表中的单个数字
#7. 写一个冒泡排序
#8. 写一个快速排序
#Python 实现一个二进制计算