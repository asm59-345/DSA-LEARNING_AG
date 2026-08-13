class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_to_idx = {}
        

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx_to_remove = self.val_to_idx[val]
        last_val = self.vals[-1]

        self.vals[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove

        self.vals.pop()
        del self.val_to_idx[val]

        return True


    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()