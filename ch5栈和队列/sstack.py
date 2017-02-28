# 基于顺序表的栈类


class StackUnderflow(ValueError):
    pass


class SStack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise StackUnderflow('The stack is empty!')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('The stack is empty!')
        return self._elems.pop()

    def depth(self):
        return len(self._elems)

#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")

    # # *************************
    # # test is_empty(),push()
    # # *************************
    # st1 = SStack()
    # print(st1.is_empty())
    # st1.push(0)
    # print(st1.is_empty())

    # # *************************
    # # test top()
    # # *************************
    # st1 = SStack()
    # #print(st1.top())
    # for i in range(0, 5):
    #     st1.push(i)
    #     print(st1.pop(), end=' ')

    # # *************************
    # # test depth()
    # # *************************
    # st1 = SStack()
    # print(st1.depth())
    # for i in range(0, 5):
    #     st1.push(i)
    #     print(st1.depth())






