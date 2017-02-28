# 循环单链表类
from lnode import LNode, LinkedListUnderflow


class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, item):
        p = LNode(item)
        if self.is_empty():
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, item):
        self.prepend(item)
        self._rear = self._rear.next

    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow('Nothing to pop!')
        p = self._rear.next
        if p.next == p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderflow('Nothing to pop!')
        p = self._rear
        if p.next == p:
            self._rear = None
            return p.elem
        else:
            while p.next != self._rear:
                p = p.next
            p.next = p.next.next
            pop_item = self._rear.elem
            self._rear = p
            return pop_item


    def printall(self):
        if self.is_empty():
            print('It is empty!')
            return
        p = self._rear.next
        print(p.elem, end=' ')
        p = p.next
        while p is not self._rear.next:
            print(p.elem, end=' ')
            p = p.next
        print()

#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")

    # # *************************
    # # test is_empty()
    # # *************************
    # list1 = LCList()
    # print(list1.is_empty())
    # list1.prepend(0)
    # print(list1.is_empty())


    # # *************************
    # # test prepend(),printall()
    # # *************************
    # list1 = LCList()
    # list1.printall()
    # for i in range(0, 5):
    #     list1.prepend(i)
    #     list1.printall()


    # # *************************
    # # test append()
    # # *************************
    # list1 = LCList()
    # for i in range(0, 5):
    #     list1.append(i)
    #     list1.printall()
    # for i in range(0, 5):
    #     list1.prepend(i)
    #     list1.printall()


    # # *************************
    # # test pop()
    # # *************************
    # list1 = LCList()
    # #list1.pop()  # 测试空表弹出
    # for i in range(0, 5):
    #     list1.append(i)
    #
    # list1.printall()
    #
    # while not list1.is_empty():
    #     print('pop item:', list1.pop())
    #     list1.printall()


    # # *************************
    # # test pop_last()
    # # *************************
    # list1 = LCList()
    # #list1.pop()  # 测试空表弹出
    # for i in range(0, 5):
    #     list1.append(i)
    #
    # list1.printall()
    #
    # while not list1.is_empty():
    #     print('pop item:', list1.pop_last())
    #     list1.printall()


