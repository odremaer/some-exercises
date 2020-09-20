# [1,0,0,1,1,1,1,0,0,0]
# def(list) => 4
# def f(list):
#     max_length = 0
#     max = 0
#     for i in list:
#         if i == 1:
#             max_length+=1
#         elif i == 0:
#             max_length = 0
#         if (max < max_length):
#             max = max_length
#
#     return max
#
#
# list = [1,0,0,1,1,1,1,1,1,1,0,0,0]
# print(f(list))











# def fib(n):
#     first = 1
#     second = 1
#     for i in range(1,n):
#         some_number = first + second
#         first = second
#         second = some_number
#     print(some_number)
#
#
# fib(5) # 1 1 2 3 5 8


# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fac(n-1)
#
#
# print(fac(5))

# def fac(n):
#     res = 1
#     i = 0
#     if n == 0:
#         return 1
#     for i in range(1,n):
#         res *= n


# def p(a):
#     def f(b):
#         def c(g):
#             return global
#
#
#
#
# # p(1)(2)(3)
#
# def p(a):
#     print(a)
#     def f(b):
#         global y
#         print(y)
#
# x = 1
# y = 2
#
# p(x)(y)
#
#
# def m(num = 1):
#     a = 0
#     def j(h = 1):
#         def c(b =1):
#             return b * h * num
#         return c
#     return j
#
# print(m(1)()(3))
#
#
#
# print(0.1 + 0.2)
#
# # print(0.1 + 0.2 != 0.3)
#
# list = [{}, {}]
#
#
# class Obj():
#     def __init__(self):
#         self.a = 1
#
#     def getA(self):
#         return self.a
#
#
# class B():
#     def __init__(self):
#         self.a = 2
#     def getA(self):
#         return self.a
# obj = Obj()
# c = obj.getA
# b = B()
# print(c)
# # obj.getA = b.getA
# print(obj.getA())
#
# # print(obj.getA() + obj.getA())
#
#
#

# class B():
#     b = 0
#     def getA(self):
#         self.b+=1
#         return self
#     def getB(self):
#         self.b+=1
#         print(self.b)
#         return self
#
#
# v = B()
# v.getA().getB()
# v.getB().getA().getB()


class Stack():
    def __init__(self, size):
        self._stack = []
        self.size = size

    def pop(self):
        # возвращает и удаляет последний элемент в списке
        # print(pop)
        print(self._stack[-1])
        self._stack.pop()
        return self

    def push(self, *param):
        self.k = 0
        self.array = param[0]

        while len(self.array) < self.size:
            self.array.append(self.array[self.k])
            self.k += 1
        self.k = 0

        for i in range(0, len(self.array)):
            self._stack.append(self.array[i])
        return self

    def getA(self):
        print(self._stack)
        return self

# class Hash(Stack):
#     {
#     0(1)
#     }


obj = Stack(5)
obj.push([1,2,3]).getA().pop().pop().pop().getA()

# 1 2 3 4
# 1 2 3 4 1 2 3 4 1 2



