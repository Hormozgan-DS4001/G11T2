class SArray:

    class NodeHandler:
        def __init__(self, array, index):
            self.array = array
            self.index = index

        def has_prev(self):
            return self.index > 0

        def has_next(self):
            return self.index < self.array.size

        def get(self):
            return self.array[self.index]

        def traverse(self, reverse=False):
            if not reverse:
                while self.index < len(self.array):
                    yield self.array[self.index]
                    self.index += 1

            else:
                while self.index >= 0:
                    yield self.array[self.index]
                    self.index += 1

    def __init__(self, size):
        self.array = size * [None]
        self.size = size

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __iter__(self):
        counter = 0

        while counter < self.size:
            yield self.size[counter]
            counter += 1


class Dll:

    class NodeHandler:
        def __init__(self, dll,  node):
            self.dll = dll
            self.node = node

        def next(self):
            self.node = self.node.start

        def prev(self):
            self.node = self.node.end

        def get(self):
            return self.node.data

        def copy(self):
            return Dll.NodeHandler(self.dll, self.node)

        def delete_node(self):

            if not self.node.start:
                self.dll.delete(len(self.dll) - 1)
            elif not self.node.end:
                self.dll.delete(0)
            else:
                self.node.start = self.node.end
                self.node.end = self.node.start
                self.dll._length -= 1

        def traverse(self, reverse=False):

            while True:
                if not reverse:
                    yield self.node
                    if not self.node.start:
                        break
                    self.node = self.node.start
                else:
                    yield self.node
                    if not self.node.end:
                        break
                    self.node = self.node.end

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        t = self.head
        while t:
            yield t.data
            t = t.start

    def delete(self, index):
        assert 0 <= index < self._length

        if self._length == 1:
            self.head = None
            self.tail = None

        elif index == 0:
            self.head = self.head.start
            self.head.prev = None

        elif index == self._length - 1:
            self.tail = self.tail.end
            self.tail.next = None

        else:
            del_node = self._get_node(index)
            del_node.perv = del_node.start
            del_node.start = del_node.end

        self._length -= 1

    def append(self, data):
        new_node = self._Node(data)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self._length += 1

    def _get_node(self, index):
        assert 0 <= index < self._length

        if self._length - index < index:
            t = self.tail
            counter = self._length - 1
            while index < counter:
                t = t.end
                counter -= 1

        else:
            t = self.head
            counter = 0
            while counter < index:
                t = t.start
                counter += 1
        return t

    def get_node_handler(self, index):
        return self.NodeHandler(self, self._get_node(index))


class DArray:
    
    class IndexHandler:
        def __init__(self, array, index):
            self.array = array
            self.index = index

        def has_next(self):
            return self.index < len(self.array)

        def has_prev(self):
            return self.index > 0

        def copy(self):
            return DArray.IndexHandler(self.array, self.index)

        def get(self):
            return self.array[self.index]

        def traverse(self, reverse=False):
            if not reverse:
                while self.index < len(self.array):
                    yield self.array[self.index]
                    self.index += 1
            else:
                while self.index >= 0:
                    yield self.array[self.index]
                    self.index -= 1

    def __init__(self, capacity=10):
        self.length = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        assert item < self.length
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def is_empty(self):
        return self.length == 0

    def append(self, data):
        if self.capacity == self.length:
            self._resize(2*self.capacity)
        self.array[self.length] = data
        self.length += 1

    def _resize(self, capacity):
        a = [None] * capacity
        for i in range(self.length):
            a[i] = self.array[i]
        self.capacity = capacity
        self.array = a

    def pop(self):
        assert not self.is_empty()
        self.length -= 1
        a = self.array[self.length]
        if self.is_empty():
            pass
        else:
            if self.capacity % self.length == 0:
                self._resize(int(self.capacity/2))
        return a

    def __repr__(self):
        return "DArray" + repr(self.array[:self.length])

    def get_node_handler(self, index=0):
        return self.IndexHandler(self, index)















