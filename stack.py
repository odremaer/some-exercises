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
obj.push([1,2,3]).getA().pop().push([4,5,6]).getA().pop()

# 1 2 3 4
# 1 2 3 4 1 2 3 4 1 2