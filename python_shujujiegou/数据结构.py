# 数据结构：不仅仅指数据在逻辑上的结构，也有在存储空间上的位置结构。
# 顺序表：有一定顺序的数据结构
# 对于基本布局顺序表：它存储相同单元大小并且在内存地址上连续的数据，逻辑地址是其元素的逻辑顺序(在表中的位置)，物理地址是第一个元素
# 的内存地址加上离第一个元素距离，如e1元素(逻辑地址为1)的物理地址为l0，那么e2的物理地址是e1的地址加上e1所占用的大小c，
# 所以en元素的物理地址就是l0+(n-1)*c

# 基本顺序链表的问题：表中的元素大小不统一，都用最大元素的的存储单元作为基本单位，浪费空间，因此出现了外置顺序表，他将
# 元素的索引以相同单元大小存储在表中，这个索引记录对应数据在内存上的地址，我们通过基本布局的方式找到元素索引，在根据索引找到数据

# python内置了一些常用的数据结构如线性表结构的list、tuple，离散结构的dict，queue的队列和堆栈的结构都是数据结构的应用，
# 只不过python将其封装成了自己的基本类。
#
# 数据结构涉及一些安全性，用链表实现队列比用列表实现队列更安全，因为链表只能从一端访问到另一端；
# 列表的尾端添加元素比头部添加元素性能更好；哈希表即字典查找元素的速度高于list。

# 顺序表和链表作为线性表的典型结构
# 数据结构-顺序表：
# 顺序表：包含两部分，一部分是顺序表的记录信息块(含顺序表的容量，元素个数)，另一部分是数据块，这两个放在一起是一体式结构
# 如果分离通过索引连接(数据块存放指向元素位置的索引)是分离式结构
#
# 因为顺序表中包含了表容量和表容量的使用情况，所以就容易实现扩容，扩容方式有两种：1.频繁的固定扩容，即每次增加固定容量
# 因此会频繁扩容。2.倍增扩容，比如2,4,8,16这种方式扩容，扩容频率低但是容易造成浪费。
#
# python中list和tuple都是顺序表结构,但list是动态顺序表支持内部结构变化如增加删除元素,而tuple不支持结构的变化,其他跟list一样
# 所以在顺序表的结尾append()增加一个元素，他的时间复杂度是O(1),insert()在n出插入一个元素相当于将插入之后的元素一次向下
# 挪动一个位置，它的时间复杂度为O(n)，pop()如果只删除末尾元素，则也是O(1)，当传入索引n，则为O(n)


# 数据结构-单向链表：
# 单向链表是线性表的其中之一，

# 节点对象
# class Node:
#     def __init__(self, item):
#         self.item = item  # 该节点值
#         self.next = None   # 该节点的链接域指向下一个节点
#
#
# # 链表对象
# class SinglyLinkedList:
#     def __init__(self):
#         self._head = None
#
#     def add(self, item):
#         """
#         头部添加节点
#         :param item: 节点的元素域(值)
#         :return:
#         """
#         node = Node(item)
#         node.next = self._head
#         self._head = node
#
#     def append(self, item):
#         """
#         尾部添加节点,需要判断是否为空链表，是空链表就用头部添加方法，不是空链表就遍历到最后一个节点上添加节点
#         :param item:
#         :return:
#         """
#         cur = self._head
#         if not cur:  # 判断是否为空链表，空链表使用头部添加方法
#             self.add(item)
#         else:
#             node = Node(item)
#             while cur.next:
#                 cur = cur.next
#             cur.next = node
#
#     @property  # 该装饰器 将函数当为属性调用
#     def is_empty(self):
#         """
#         判断链表是否为空，只需要看头部是否有节点
#         :return:
#         """
#         if self._head: # 头部有节点
#             return False
#         else:
#             return True
#
#     def length(self):
#         cur = self._head
#         n = 0
#         if not cur:  # 为空链表返回0
#             return n
#         else:
#             while cur.next:
#                 cur = cur.next
#                 n += 1
#             return n+1
#
#     def ergodic(self):
#         """
#         遍历链表
#         :return:
#         """
#         cur = self._head
#         if not cur:
#             print('None')
#         else:
#             while cur.next:
#                 cur = cur.next
#             print(cur.item)
#
#     def insert(self, index, item):
#         """
#         在指定位置插入节点(索引从0开始)
#         :param index:
#         :param item:
#         :return:
#         """
#         if index == 0:  # 当索引为0时头部插入
#             self.add(item)
#         elif index >= self.length:  # 当索引超范围则尾部插入
#             self.append(item)
#         else:  # 找到插入位置的上一个节点，修改上一个节点的next属性
#             cur = self._head
#             n = 1
#             while cur.next:
#                 if n == index:
#                     break
#                 cur = cur.next
#                 n += 1
#             node = Node(item)
#             node.next = cur.next
#             cur.next = node
#
#     def delete(self, item):
#         """
#         删除节点
#         :param item:
#         :return:
#         """
#         if self.is_empty:  # 当节点是空时
#             raise ValueError("null")
#         cur = self._head
#         pre = None  # 记录删除节点的上一个节点
#         if cur.item == item:  # 当删除节点为第一个的情况
#             self._head = cur.next
#         while cur.next:
#             pre = cur
#             cur = cur.next
#             if cur.item == item:
#                 pre.next = cur.next
#
#     def search(self, item):
#         """
#         查看节点是否存在
#         :param item:
#         :return:
#         """
#         cur = self._head
#         while None != cur:
#             if cur.item == item:
#                 return True
#             cur = cur.next
#         return False

# 单向循环链表解决约瑟夫环
# 使用一个计数器解决约瑟夫环
# def f(n, m):
#     list1 = []
#     for i in range(1,n+1):
#         list1.append(i)
#     index = 0  # 被删除的元素索引
#     count = 0  # 计数器
#     while len(list1) > 1:
#         count += 1
#         # 当报数来到了队列的尾部，我们需要从队列的第一个元素开始报数，此时重置索引
#         if index >= len(list1):
#             index = 0
#         # 开始循环报数，将序号为m的人移除队列
#         if count >= m:
#             # 移除队列，计数器置0
#             list1.pop(index)
#             count = 0
#             index -= 1
#         index += 1
#     return list1[0]
#
#
# print(f(100, 3))


# 数学归纳法解决约瑟夫环
# def f(n,m):
#     if n == 1:
#         return 0
#     return (f(n-1,m)+m)%n


# print(f(10000, 30))


# 数据结构-单向循环链表数据结构
# 在单向链表的基础上，最后一个节点指向头部，定义基本节点对象和链表对象。
class Node:
    def __init__(self, item):
        self.item = item  # 该节点值
        self.next = None  # 连接下一个节点


class SingleCyLinkedList:
    def __init__(self):
        self._head = Node

    @property
    def is_empty(self):
        """
        是否为空链表
        :return:
        """
        return None == self._head

    def length(self):
        """
        链表长度
        :return:
        """
        if self.is_empty:
            return 0
        n = 1
        cur = self._head
        while cur != self._head:
            cur = cur.next
            n += 1
        return 1














