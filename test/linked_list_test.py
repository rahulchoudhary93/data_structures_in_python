import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.pardir), "singly_linked_list"))

from data_structures_in_python.singly_linked_list import LinkedList

linkedlist = LinkedList()
linkedlist.prepend(12)
linkedlist.prepend(13)
linkedlist.list_size()
linkedlist.delete(12)
linkedlist.list_size()
linkedlist.append(14)
linkedlist.append(15)
linkedlist.insert(2, 1)
linkedlist.list_size()
linkedlist.display()