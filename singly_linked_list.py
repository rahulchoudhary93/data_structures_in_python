class LinkedListNode(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def display(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.get_data())
            current_node = current_node.get_next_node()
        print(nodes)
        return nodes

    def prepend(self, data):
        new_node = LinkedListNode(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def list_size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next_node()
        print(count)
        return count

    def delete(self, data):
        current_node = self.head
        previous_node = None
        found = False
        while current_node:
            if current_node.get_data() == data:
                if not previous_node:
                    self.head = current_node.get_next_node()
                else:
                    previous_node.set_next_node(current_node.get_next_node())
                found = True
                break
            else:
                previous_node = current_node
                current_node = current_node.get_next_node()
        if not found:
            raise ValueError("The given element is not found in the list")
        else:
            print("The element with data {} has been deleted. Data provided is {}.".format(current_node.get_data(), data))

    def append(self, data):
        current_node = self.head
        if not self.head:
            self.head = LinkedListNode(data)
        else:
            while current_node.get_next_node():
                current_node = current_node.get_next_node()
                print("curr", current_node)
            current_node.set_next_node(LinkedListNode(data))

    def insert(self, data, position):
        current_node = self.head
        previous_node = None
        count = 1
        while count is not position:
            previous_node = current_node
            current_node = current_node.get_next_node()
            count += 1
        print(previous_node, current_node)
        new_node = LinkedListNode(data)
        if not previous_node:
            new_node.set_next_node(self.head)
            self.head = new_node
        else:
            previous_node.set_next_node(new_node)
            new_node.set_next_node(current_node)



