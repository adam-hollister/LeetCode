"""
All operations must be O(1) time.
To hit O(1) for both get and put, we need:

Fast lookup by key → use a HashMap

Fast reordering by usage → use a Doubly Linked List

We track usage order from most recently used (head) to least recently used (tail).

"""
class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None
        self.prev = None

class LinkedListCustom:
    def __init__(self, capacity: int):
        #hashmap for lookup by key to get a node
        my_hashmap = {int, Node}
        # doubly linked list
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value): # add to end
        new_node = Node(value)
        if not self.head:               # list is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, key, value): # add to front
        new_node = Node()
        new_node.key = key
        new_node.value = value
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_after(self, node, value):
        if node is None:
            return  # or raise an error
        new_node = Node(value)
        nxt = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = nxt
        if nxt:
            nxt.prev = new_node
        else:
            self.tail = new_node
        self.size += 1

    def remove(self, node):
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:                  # node is head
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:                  # node is tail
            self.tail = node.prev
        self.size -= 1
        # optionally clear pointers:
        node.prev = node.next = None

    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.value, end=" ↔ ")
            curr = curr.next
        print("None")

    def traverse_backward(self):
        curr = self.tail
        while curr:
            print(curr.value, end=" ↔ ")
            curr = curr.prev
        print("None")

class Solution:
    def __init__(self, capacity: int):
        #hashmap for lookup by key to get a node
        self.my_hashmap = {}
        self.linkedList = LinkedListCustom(capacity)

    # given a key return the value or -1 if it doesn't exist
    def getKey(self, key:int) -> int:
        value = self.my_hashmap.get(key)
        if value:
            return value
        return -1

    # insert or update the key, evict least recently used if capacity is exceeded
    def put(self, key: int, value: int):
        #If key is not present
        dummyNode = self.linkedList.head
        node = Node()
        node.key = key
        node.value = value
        if self.my_hashmap.get(key): #delete and re add
            print("found")
            # move the item to the front of the linked list
            while dummyNode.key != key:
                dummyNode = dummyNode.next
                print(dummyNode.value)
            self.linkedList.remove(dummyNode)
        self.linkedList.prepend(key, value)
        self.my_hashmap[key] = value

        #If the key is already present, you update its value and mark it as recently used
        #If it's not, you add a new entry and possibly evict the least recently used one
        print("put")

if __name__ == "__main__":
    sol = Solution(5)
    sol.put(1, 19)
    assert sol.getKey(1) == 19, "Test Case 1 Failed!"
    sol.put(2, 3)
    sol.put(3, 9)
    sol.put(4, 89)
    sol.put(4, 39)

    assert sol.getKey(8) == -1, "Test Case 3 Failed!"
    #assert sol.put(3, 3), "Test Case 2 Failed!"

    print("all tests passed")