class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        num_items = 0
        oldest = None

    def append(self, item):
        if self.data:
            if self.num_items < self.capacity:
                self.data.append(item)
                self.num_items += 1
            else:
                self.data[self.oldest] = item
                self.oldest += 1
                if self.oldest >= self.capacity:
                    self.oldest = 0
        else:
            self.data.append(item)
            self.oldest = 0
            self.num_items = 1

    def get(self):
        # Return a list of elements from the oldest to the newest. 
        return self.data

#     buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']