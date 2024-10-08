class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k 
        self.front = None
        self.rear = None
        self.size = 0  

    def insertFront(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        
        if self.front is None:  
            n = Node(value)
            self.front = n
            self.rear = n
            self.front.prev = self.front
            self.front.next = self.front
        else:  
            n = Node(value, self.rear, self.front)
            self.front.prev = n
            self.rear.next = n
            self.front = n

        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        
        if self.front is None:  
            n = Node(value)
            self.front = n
            self.rear = n
            self.front.prev = self.front
            self.front.next = self.front
        else: 
            n = Node(value, self.rear, self.front)
            self.front.prev = n
            self.rear.next = n
            self.rear = n

        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:  
            self.front = None
            self.rear = None
        else:
            temp = self.front.next
            self.rear.next = temp
            temp.prev = self.rear
            self.front = temp

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:  
            self.front = None
            self.rear = None
        else:
            temp = self.rear.prev
            temp.next = self.front
            self.front.prev = temp
            self.rear = temp

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()