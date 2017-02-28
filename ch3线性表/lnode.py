# 单链表结点类


class LinkedListUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None ):
        self.elem = elem
        self.next = next_

    def __str__(self):
        return str(self.elem)

#--------------------------------
if __name__ == "__main__":

    def length(head):
        p = head
        n = 0
        while p is not None:
            n += 1
            p = p.next
        return n

    list1 = LNode(1)
    p = list1

    for i in range(2, 6):
        p.next = LNode(i)
        p = p.next

    print(length(list1))

    p = list1
    while p is not None:
        print(p.elem, end=',')
        p = p.next





