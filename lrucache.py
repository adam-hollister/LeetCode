"""
All operations must be O(1) time.
To hit O(1) for both get and put, we need:

Fast lookup by key → use a HashMap

Fast reordering by usage → use a Doubly Linked List

We track usage order from most recently used (head) to least recently used (tail).

"""
class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

class LinkedListCustom:
    def __init__(self, capacity: int):
        #hashmap for lookup by key to get a node
        my_hashmap = {int, Node}
        # doubly linked list
        self.head = Node()
        self.tail = Node()

    def insertNode(self, previousNode: Node, nodeToBeAdded: Node, value: int):
        nodeToBeAdded = Node()
        nodeToBeAdded.value = value
        nodeToBeAdded.next = self.head.next
        nodeToBeAdded.prev = self.head
        self.head.next.prev = nodeToBeAdded
        self.head.next = nodeToBeAdded

class Solution:
    def __init__(self, capacity: int):
        #hashmap for lookup by key to get a node
        my_hashmap = {int, LinkedListCustom}

    # given a key return the value or -1 if it doesn't exist
    def getKey(self, key:int) -> int:
        return -1

    # insert or update the key, evict least recently used if capacity is exceeded
    def put(self, key: int, value: int):
        #If key is not present


        #If the key is already present, you update its value and mark it as recently used
        #If it's not, you add a new entry and possibly evict the least recently used one
        print("put")

if __name__ == "__main__":
    sol = Solution(5)
    assert sol.getKey(8) == -1, "Test Case 1 Failed!"
    #assert sol.put(3, 3), "Test Case 2 Failed!"

    print("all tests passed")