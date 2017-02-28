# 单链表类
from lnode import LNode, LinkedListUnderflow


class LList:
    def __init__(self, ):
        self._head = None

    def clear(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        p = self._head
        n = 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('there is no node in the list!')
        e = self._head.elem
        self._head = self._head.next
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("Nothing to pop!")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def delete(self, index):
        if self._head is None:
            raise LinkedListUnderflow('Nothing to delete!')
        if index == 0:
            return self.pop()
        p = self[index-1]
        if p.next is None:
            raise LinkedListUnderflow('Index error!')
        e = p.next.elem
        p.next = p.next.next
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print(end='\n')

    def __getitem__(self, i):
        if i < 0:
            raise LinkedListUnderflow('index error')
        p = self._head
        while p is not None and i > 0:
            i -= 1
            p = p.next
        if p is None:
            raise LinkedListUnderflow('index error')
        else:
            return p

    def elments(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")

    # # *************************
    # # test clear()
    # # *************************
    # list1 = LList()
    # for i in range(1, 10):
    #     list1.prepend(i)
    # print(list1.is_empty())
    # list1.clear()
    # print(list1.is_empty())


    # # *************************
    # # test is_empty(),prepend()
    # # *************************
    # list1 = LList()
    # print(list1.is_empty())
    #
    # for i in range(1, 10):
    #     list1.prepend(i)
    #
    # print(list1.is_empty())
    #
    # list1.printall()


    # # *************************
    # # test length()
    # # *************************
    # list1 = LList()
    # print(list1.length())
    # list1.append(1)
    # print(list1.length())
    # list1.append(1)
    # print(list1.length())
    # list1.pop_last()
    # print(list1.length())


    # # *************************
    # # test append()
    # # *************************
    # list1 = LList()
    # for i in range(0, 5):
    #     list1.append(i)
    #
    # for x in list1.elments():
    #     print(x, end=' ')


    # # *************************
    # # test insert()
    # # *************************
    # list1 = LList()
    # # 测试空表状态下的插入
    # # list1.insert(88, index = -1) #测试表为空时，在非0处插入是否会报错
    # # list1.insert(88, index=1) #测试表为空时，在非0处插入是否会报错
    #
    # list2 = LList()
    # for i in range(0, 10):
    #     list2.insert(i, index=i)
    # print(end='\n')
    # for x in list2.elments():
    #     print(x, end=' ')
    # # list2.insert(88, index=11)  # 测试越界插入是否会报错
    # # list2.insert(88, index=-1)  # 测试越界插入是否会报错
    # list2.insert(88, index=7)
    # print(end='\n')
    # for x in list2.elments():
    #     print(x, end=' ')
    #
    # list3 = LList()
    # for i in range(0, 10):
    #     list3.insert(i, index=0)
    # print(end='\n')
    # for x in list3.elments():
    #     print(x, end=' ')


    # # *************************
    # # test pop()
    # # *************************
    # list1 = LList()
    # #list1.pop()  #测试空表弹出是否会报错
    #
    # for i in range(1, 5):
    #     list1.prepend(i)
    #
    # while not list1.is_empty():
    #     print(list1.pop())
    #
    # list1.pop()


    # # *************************
    # # test pop_last()
    # # *************************
    # list1 = LList()
    # #list1.pop_last()  #测试空表弹出是否会报错
    # for i in range(0,5):
    #     list1.append(i)
    #
    # for i in range(0,5):
    #     print(list1.pop_last())


    # # *************************
    # # test delete()
    # # *************************
    # list1 = LList()
    # for i in range(0, 5):
    #     list1.append(i)
    # # list1.delete(5)    # 测试越界删除是否报错
    # # list1.delete(-1)   # 测试越界删除是否报错
    # for x in list1.elments():
    #     print(x, end=',')
    #
    # print(end='\n')
    #
    # for i in range(0, 5):  # 测试从头删除
    #     list1.delete(0)
    #     for x in list1.elments():
    #         print(x, end=',')
    #     print(end='\n')
    #
    # print(list1.is_empty())
    # # list1.delete(0)  # 测试空表删除是否报错
    # # list1.delete(1)  # 测试空表删除是否报错
    #
    # list2 = LList()
    # for i in range(0, 5):
    #     list2.append(i)
    #
    # for x in list2.elments():
    #     print(x, end=',')
    #
    # print(end='\n')
    #
    # for i in range(5, 0, -1):    # 测试从尾部删除
    #     list2.delete(i-1)
    #     for x in list2.elments():
    #         print(x, end=',')
    #     print(end='\n')
    #
    # print(end='\n')
    #
    # list3 = LList()
    # for i in range(0, 5):
    #     list3.append(i)
    #
    # for x in list3.elments():
    #     print(x, end=',')
    #
    # list3.delete(1)    # 测试随机删除
    # print(end='\n')
    # for x in list3.elments():
    #     print(x, end=',')
    # list3.delete(2)    # 测试随机删除
    # print(end='\n')
    # for x in list3.elments():
    #     print(x, end=',')
    # list3.delete(1)    # 测试随机删除
    # print(end='\n')
    # for x in list3.elments():
    #     print(x, end=',')
    # list3.delete(1)    # 测试随机删除
    # print(end='\n')
    # for x in list3.elments():
    #     print(x, end=',')

    # # *************************
    # # test find()
    # # *************************
    # list1 = LList()
    # print(list1.find(lambda x: x == 0))
    #
    # list1.append(0)
    # print(list1.find(lambda x: x == 0))
    # print(list1.find(lambda x: x == 1))
    #
    # list2 = LList()
    # for i in range(0, 10):
    #     list2.append(i)
    # print(list2.find(lambda x: x % 2 == 0))
    # print(list2.find(lambda x: x - 3 == 2))

    # # *************************
    # # test filter()
    # # *************************
    # list1 = LList()
    # for x in list1.filter(lambda y: y == 0):
    #     print(x)
    #
    # list1.append(0)
    # for x in list1.filter(lambda y: y == 0):
    #     print(x)
    # for x in list1.filter(lambda y: y == 1):
    #     print(x)
    #
    # list2 = LList()
    # for i in range(0, 10):
    #     list2.append(i)
    # for x in list2.filter(lambda y: y % 2 == 0):
    #     print(x, end=' ')
    # print()
    # for x in list2.filter(lambda y: y % 2 == 1):
    #     print(x, end=' ')

    # # *************************
    # # test __getitem__()
    # # *************************
    # list1 = LList()
    # #list1[0]  #测试空表访问是否会报错
    # #list1[1]  #测试空表访问是否会报错
    #
    # for i in range(0, 5):
    #     list1.prepend(i)
    # #print(list1[5])  #测试越界访问是否会报错
    # for i in range(0, 5):
    #     print(list1[i], end=' ')
