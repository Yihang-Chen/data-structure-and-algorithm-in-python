from lnode import LNode, LinkedListUnderflow
from llist import LList


class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def insert(self, elem, index):
        #先略

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("Nothing to pop!")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self._rear = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

    def delete(self, index):
        #先略


#------------------------------------------
if __name__ == "__main__":

    # # *************************
    # # test prepend()
    # # *************************
    # list1 = LList1()
    # for i in range(0, 5):
    #     list1.prepend(i)
    #     print(list1._rear)
    # list1.printall()


    # # *************************
    # # test append()
    # # *************************
    # list1 = LList1()
    # for i in range(0, 5):
    #     list1.append(i)
    #     print(list1._rear)
    # list1.printall()


    # # *************************
    # # test pop_last()
    # # *************************
    # list1 = LList1()
    # #list1.pop_last()  #  测试空表弹出是否会报错
    # for i in range(0, 5):
    #     list1.append(i)
    #
    # list1.printall()
    #
    # while not list1.is_empty():
    #     print('pop:', list1.pop_last())
    #     print('last node:', list1._rear)


