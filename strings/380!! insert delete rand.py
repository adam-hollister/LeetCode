import random
class RandomizedSet:
    def __init__(self):
        self.nums = [] # list to support the random
        self.dic = {} # dictionary hashmap to support insert remove
    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.nums.append(val)
        self.dic[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        # get
        idx = self.dic[val]
        last_element = self.nums[len(self.nums)-1]
        # update
        self.nums[idx] = last_element
        self.dic[last_element] = idx
        #remove
        self.nums.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    sol = RandomizedSet()
    assert sol.insert(0) == True, "Failed 1"
    assert sol.insert(1) == True, "Failed 2"
    assert sol.remove(0) == True, "Failed 3"
    print("all tests passed")