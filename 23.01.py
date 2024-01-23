# from typing import NamedTuple
#
#
# class UserInfo(NamedTuple):
#     name: str
#     age: int
#     id: int
#
#
# u = UserInfo(name="Вася", age=5, id=5454)

# from dataclasses import dataclass
#
#
# @dataclass
# class User:
#     name: str
#     age: int
#     id: int
#
#
# user = User(name='pet', age=15, id=1)

# import heapq
#
#
# class Node:
#     def __init__(self, v, left=None, right=None):
#         self.v = v
#         self.left = left
#         self.right = right
#
#
# class Tree:
#     def __init__(self, root: Node = None):
#         self.root = root
#
#     def add(self):
#         pass
# from typing import List
# import heapq
#
# lst = [99, 5, 85, 19]
# heapq.heapify(lst)
# print(heapq.nlargest(2, lst))
#
# n, k = map(int, input().split())
# lst = list(map(int, input().split()))
#
#
# def foo(n: int, k: int, lst: List[int]):
#     heap = []
#     for i, num in enumerate(lst):
#         num = str(num)
#         for _i, temp_num in enumerate(num):
#             v = int(temp_num) * (10 ** (len(num) - _i - 1))
#             old_num = int(num)
#             old_num -= v
#             old_num += 9 * (10 ** (len(num) - _i - 1))
#             heapq.heappush(heap, old_num - int(num))
#     return heap
#
#
# h = foo(n, k, lst)
#
# print(sum(heapq.nlargest(k, h)))

# 2

# res = [4, 10, 4, 80, 0]
# O(n*k)

# for item in lst:
#     str_num = str(item)
#     for i in item:

# print(hash("5"))
# print(hash("5") % 10)
from collections import deque


class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __str__(self):
        return f"k: {self.k}, v: {self.v}"


class MyDict:
    def __init__(self):
        self.lst = [None for _ in range(10)]
        self.size = 0

    def add(self, k, v):
        index: int = hash(k) % len(self.lst)

        if self.lst[index] is None:
            self.lst[index] = Node(k=k, v=v)
            return

        if isinstance(self.lst[index], deque):
            for item in self.lst[index]:
                if item.k == k:
                    item.v = v
                    return
            self.lst[index].append(Node(k=k, v=v))
            return

        if self.lst[index].k == k:
            self.lst[index].v = v
            return

        temp_lst = deque()
        temp_lst.append(self.lst[index])
        temp_lst.append(Node(k=k, v=v))
        self.lst[index] = temp_lst

    def __str__(self):
        return str(self.lst)

d = {}

d.get()
d.pop()
d.clear()
