# 基于list的循环队列
class QueueUnderflow(ValueError):
    pass


class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = ['*'] * self._len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self.is_empty():
            raise QueueUnderflow('Nothing in queue!')
        return self._elems[self._head]

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow('Nothing in queue!')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend( )
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = ['*']*self._len
        for i in range(0, old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems = new_elems
        self._head = 0


#------------------------------------------
if __name__ == "__main__":

    print("Start testing.")
    queue1 = SQueue()

    for k in range(7):
        for i in range(2**k):
            queue1.enqueue(i + 1)
        while not queue1.is_empty():
            print(queue1.dequeue(), end=' ')
        print()

    for k in range(7, -1, -1):
        for i in range(2**k):
            queue1.enqueue(i + 1)
        while not queue1.is_empty():
            print(queue1.dequeue(), end=' ')
        print()











