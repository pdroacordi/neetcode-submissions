class MyHashMap:

    def __init__(self):
        self.size    = 1009
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)

        if self.buckets[idx] is None:
            self.buckets[idx] = [[key, value]]
        else:
            for kv in self.buckets[idx]:
                if kv[0] == key:
                    kv[1] = value
                    return
            self.buckets[idx].append(tuple((key,value)))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        
        if self.buckets[idx] is None:
            return -1

        for kv in self.buckets[idx]:
            if kv[0] == key:
                return kv[1]
        
        return -1
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)

        if self.buckets[idx] is None:
            return

        for kv in self.buckets[idx]:
            if kv[0] == key:
                self.buckets[idx].remove(kv)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)