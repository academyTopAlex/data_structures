from abc import ABC, abstractmethod
import collections
import random

# list_of_letters = list('абракадабра')
# letter_cnt = collections.Counter(list_of_letters)
# print(letter_cnt["d"])

# emotion_cnt = collections.Counter({'like':2, 'dislike':3})
# print(emotion_cnt)#Counter({'like': 2, 'dislike': 3})

# print(list(emotion_cnt.elements())) #['like', 'like', 'dislike', 'dislike', 'dislike']

# print(letter_cnt.most_common(3))# [('а', 5), ('б', 2), ('р', 2)])
# print(letter_cnt.most_common()[-2:])

# >>> sum(letter_cnt.values())  # число всех посчитанных элементов
# 11
# >>> list(letter_cnt)  # список уникальных элементов исходной последовательности
# ['а', 'б', 'р', 'к', 'д']
# >>> set(letter_cnt)
# {'а', 'б', 'д', 'к', 'р'}
# >>> dict(letter_cnt)  # счетчик это подкласс словаря, можно преобразовать в обычный dict
# {'а': 5, 'б': 2, 'р': 2, 'к': 1, 'д': 1}


# d = collections.defaultdict(int)
# d['name'] = 'James' 
# d['surname'] = 'Bond'
# d['patronymic']
# ''
# print(d)# defaultdict(str, {'name': 'James', 'surname': 'Bond', 'patronymic': ''})



# OrderedDict
'''
   popitem(last=True) – удаляет последний элемент если last=True, и первый, если last=False
   move_to_end(key, last=True) – переносит ключ key в конец, если last=True, и в начало, если last=False 
'''

# d = collections.OrderedDict.fromkeys('abcde')
# print(d)
# d.move_to_end('b')
# print(d)
# print(''.join(d.keys()))
# d.move_to_end('b', last=False)
# print(d)
# print(''.join(d.keys()))


# deque

# Пример компактной и быстрой реализации функции скользящего среднего
def moving_average(lst:list[int|float], n:int=3) -> list[float]:
   deque = collections.deque(lst[:3])
   s = sum(deque)
   res = [s / n]

   for item in lst:
      s += item - deque.popleft()
      deque.append(item)
      res.append(s / n)
   return res
(moving_average([random.randint(1,100) for i in range(1_000_000)]))


#namedtuple()


"""
   UserDict, UserList, UserString – не заслуживающие развёрнутого описания обертки над стандартными 
   объектами словарей, списков и строк для беспроблемного наследования (прямое наследование встроенным 
   типам dict, list, str чревато ошибками, связанными с игнорированием переопределения методов).
"""

class Test1(ABC):
   @abstractmethod
   def foo(seld):
      pass


class Test2(Test1):
   # def foo(seld):
   #    pass
   def foo1(seld):
      pass

t2 = Test2()
t2.foo1()