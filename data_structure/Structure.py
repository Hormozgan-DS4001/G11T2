class SArray:

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
            self.node = self.node.next

        def prev(self):
            self.node = self.node.prev

        def get(self):
            return self.node.data

        def copy(self):
            return Dll.NodeHandler(self.dll, self.node)

        def delete_node(self):

            if not self.node.next:
                self.dll.delete(len(self.dll) - 1)
            elif not self.node.prev:
                self.dll.delete(0)
            else:
                self.node.next = self.node.prev
                self.node.prev = self.node.next
                self.dll._length -= 1

        def traverse(self, reverse=False):

            while True:
                if not reverse:
                    yield self.node
                    if not self.node.next:
                        break
                    self.node = self.node.next
                else:
                    yield self.node
                    if not self.node.prev:
                        break
                    self.node = self.node.prev

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

    def delete(self, index):
        assert 0 <= index < self._length

        if self._length == 1:
            self.head = None
            self.tail = None

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None

        elif index == self._length - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            del_node = self._get_node(index)
            del_node.perv = del_node.next
            del_node.next = del_node.prev

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
                t = t.prev
                counter -= 1

        else:
            t = self.head
            counter = 0
            while counter < index:
                t = t.next
                counter += 1
        return t



















