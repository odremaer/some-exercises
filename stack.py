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
        k = 0
        array = param[0]
        while len(array) < self.size:
            array.append(array[k])
            k += 1
        k = 0

        for i in range(0, len(array)):
            self._stack.append(array[i])
        return self

    def getA(self):
        print(self._stack)
        return self

# class Hash(Stack):
#     {
#     0(1)
#     }


obj = Stack(5)
obj.push([1,2,3,4]).getA().pop().push([4,5,6]).getA().pop()

# 1 2 3 4
# 1 2 3 4 1 2 3 4 1 2