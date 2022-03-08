# when a local memory limit is hit, arrays copy over entire
# initial array to a new memory space, this takes 0(n) time.
# linked lists solve this problem by the use of nodes and links
# each node contains data and a pointer containing memory address
# of the next node which can be anywhere in the memory space


class Node:
    # data, <pointer>nextNode
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # 0(1)
    def insert_at_front(self, data):
        # create a node whose next is cur head
        node = Node(data, self.head)
        # then set that node as the head
        self.head = node

    # 0(n) - non empty list
    def insert_at_end(self, data):
        # if list empty, set head to new node - 0(n)
        if self.head is None:
            node = Node(data, None)
            self.head = node

        # else iterate until end
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            node = Node(data, None)
            itr.next = node

    # 0(n)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # 0(n)
    def remove_at(self, del_index):
        if del_index < 0 or del_index >= len(self):
            raise Exception("invalid index")

        # since python does garbage collection, there is no
        # need to worry abt memory taken by the erased nodes

        # if first node, set next node as first node
        if del_index == 0:
            self.head = self.head.next
            return

        # else iterate until index
        index = 0
        itr = self.head

        while itr:
            # stop at prev node, set next = next.next
            if index == del_index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            index += 1

    # 0(n)
    def insert_at(self, ins_index, data):
        if ins_index < 0 or ins_index > len(self):
            raise Exception("invalid index")

        if ins_index == 0:
            self.insert_at_front(data)
            return

        # else iterate until index
        index = 0
        itr = self.head

        while itr:
            # stop at prev node, set next = new node
            if index == ins_index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            index += 1

    # 0(n)
    def __len__(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # 0(n)
    def __str__(self):
        # if list empty, return error msg
        if self.head is None:
            raise Exception("list is empty")

        # else, while itr is not null
        itr = self.head
        out_str = ""
        while itr:
            out_str += str(itr.data) + " ==> "
            itr = itr.next

        return out_str + "END"
