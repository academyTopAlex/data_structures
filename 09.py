# class Bok:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def set_x(self, v):
#         self.__x = v
#
#     def get_x(self):
#         return self.__x
#
#     def __str__(self):
#         return f"{self.__x}, {self.__y}"


# x = Bok(1, 5)
# print(x)
# x.set_x(9)
# print(x)
# print(x.get_x())


# lst = list()


class Node:
    def __init__(self, data, next_link=None, pref_link=None):
        self.__data = data
        self.__next_link: Node = next_link
        self.pref_link: Node = pref_link

    def __str__(self):
        return f"{self.__data}"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, v):
        if v is None:
            raise TypeError("Not use None")
        self.__data = v

    @property
    def link(self):
        return self.__next_link

    @link.setter
    def link(self, v):
        if not isinstance(v, type(self)):
            raise TypeError("is not Node")
        self.__next_link = v

    def del_link(self):
        self.__next_link = None


# tail = Node(1)
# n2 = Node(2, tail)
# n3 = Node(3, n2)
# n4 = Node(4)
# head = Node(5, n4)


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head: Node = head
        self.tail: Node = tail
        self.len: int = 0

    # def append(self, v) -> Node:
    #     new_node = Node(v)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #         self.len += 1
    #         return new_node
    #     self.tail.link = new_node
    #     self.tail = new_node

    def append(self, v):
        new_node = Node(v)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.len += 1
            return new_node
        new_node.pref_link = self.tail
        self.tail.link = new_node
        self.tail = new_node
        self.len += 1
        return new_node

    def pop(self):
        if self.head is None:
            return

        temp_link = self.head

        while temp_link.link.link is not None:
            temp_link = temp_link.link

        temp_link.del_link()
        self.tail = temp_link

    def rev_print(self):
        temp = self.tail
        for _ in range(self.len):
            print(temp, end=" ")
            temp = temp.pref_link

    def search(self, v):
        pass

    def replace(self):
        pass

    def __str__(self):
        if self.head is None:
            return "тут пусто"
        return self.head.__str__()


lst = LinkedList()
lst.append(5)
lst.append(9)
lst.append("999")
lst.append("ejfrjeuifj")
lst.append("322")
lst.append("rerer")
lst.rev_print()
print(lst)

# while True:
#     x = int(input())
#     if x == 0:
#         break
#     lst.append(x)
# #
# nums = map(int, input().split())
# for i in nums:
#     lst.append(i)
