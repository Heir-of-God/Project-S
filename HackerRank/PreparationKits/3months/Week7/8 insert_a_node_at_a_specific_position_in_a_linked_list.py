import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)
    if position == 0:
        node.next = llist
        return node

    to_connect = llist
    for _ in range(position - 1):
        to_connect = to_connect.next

    tmp = to_connect.next
    to_connect.next = node
    node.next = tmp

    return llist


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head, " ", fptr)
    fptr.write("\n")
    fptr.close()
