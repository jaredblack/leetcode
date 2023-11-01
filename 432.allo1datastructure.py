# try this with a doubly linked list instead. each node 
# represents a frequency of words, and has a set of those
# words with that frequency

class FreqNode:
    def __init__(self, next=None, prev=None, key_set=None):
        self.next = next
        self.prev = prev
        self.key_set = key_set


from collections import defaultdict
class AllOne:

    def __init__(self):
        self.head = FreqNode()
        self.tail = FreqNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freq_to_node = {0:self.head}
        self.key_counter = defaultdict(int)



    def inc(self, key: str) -> None:     
        self.key_counter[key] += 1
        freq = self.key_counter[key]
        if freq in self.freq_to_node:
            self.freq_to_node[freq].key_set.add(key)
        else:
            self._insert_after(FreqNode(None, None, {key}), freq - 1)
        if freq > 1:
            self.freq_to_node[freq - 1].key_set.remove(key)
        if self.freq_to_node[freq - 1].key_set != None and len(self.freq_to_node[freq - 1].key_set) == 0:
            self._remove(self.freq_to_node[freq - 1])
            self.freq_to_node.pop(freq - 1)
        


    def dec(self, key: str) -> None: 
        self.key_counter[key] -= 1
        freq = self.key_counter[key]
        self.freq_to_node[freq + 1].key_set.remove(key)
        if freq not in self.freq_to_node:
            self._insert_before(FreqNode(None, None, {key}), freq + 1)
        else:
            if freq > 0:
                self.freq_to_node[freq].key_set.add(key)
        if self.freq_to_node[freq + 1].key_set != None and len(self.freq_to_node[freq + 1].key_set) == 0:
            self._remove(self.freq_to_node[freq + 1])
            self.freq_to_node.pop(freq + 1)          


    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.key_set)) if self.tail.prev.key_set != None else ''

    def getMinKey(self) -> str:
        return next(iter(self.head.next.key_set)) if self.head.next.key_set != None else ''

    def _insert_after(self, node, freq):
        prev = self.freq_to_node[freq]
        node.prev = prev
        node.next = prev.next
        prev.next = node
        if node.next:
            node.next.prev = node
        self.freq_to_node[freq + 1] = node

    def _insert_before(self, node, freq):
        next = self.freq_to_node[freq]
        node.next = next
        node.prev = next.prev
        next.prev = node
        if node.prev:
            node.prev.next = node
        self.freq_to_node[freq - 1] = node

    def _remove(self, node):
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

    def print_ll(self):
        curr = self.head
        while curr:
            print(id(curr)%1000, end=', ')
            curr = curr.next
        curr = self.tail
        print()
        while curr:
            print(id(curr)%1000, end=', ')
            curr = curr.prev
        print()

    



# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('b')
obj.inc('b')
obj.dec('b')
obj.dec('b')
print(obj.getMaxKey())
print(obj.getMinKey())

# obj.inc('hello')
# obj.inc('goodbye')
# obj.inc('goodbye')
# obj.dec('goodbye')
# obj.dec('goodbye')
# print(obj.getMaxKey())