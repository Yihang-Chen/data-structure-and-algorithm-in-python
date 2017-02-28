# 基于堆的优先队列
class PrioQueueError(ValueError):
    pass

class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return len(self._elems) == 0

    def peek(self):
        if self.is_empty:
            raise PrioQueueError('Nothing to peek!')
        else:
            return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('Nothing to dequeue!')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, 2*begin+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2-1, -1, -1):
            self.siftdown(self._elems[i], i, end)

#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")
    # # *************************
    # # test is_empty()
    # # *************************
    # prioqueue1 = PrioQueue()
    # print(prioqueue1.is_empty())
    # prioqueue1.enqueue(1)
    # print(prioqueue1.is_empty())

    # # *************************
    # # test enqueue(),dequeue()
    # # *************************
    # import random
    # prioqueue1 = PrioQueue()
    # for i in range(0, 100):
    #     prioqueue1.enqueue(random.randint(0, 100))
    # while not prioqueue1.is_empty():
    #     print(prioqueue1.dequeue(), end=' ')

    # # *************************
    # # test __init()__
    # # *************************
    # import random
    # list1 = []
    # for i in range(0, 50):
    #     list1.append(random.randint(0, 100))
    # prioqueue1 = PrioQueue(list1)
    # while not prioqueue1.is_empty():
    #     print(prioqueue1.dequeue(), end=' ')




