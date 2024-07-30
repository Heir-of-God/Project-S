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

def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    to_connect = dummy

    while head1 or head2:
        val1 = head1.data if head1 else 1001
        val2 = head2.data if head2 else 1001

        if val1 <= val2:
            to_connect.next = head1
            head1 = head1.next
        else:
            to_connect.next = head2
            head2 = head2.next

        to_connect = to_connect.next

    return dummy.next


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    tests = int(input())
    for tests_itr in range(tests):
        llist1_count = int(input())
        llist1 = SinglyLinkedList()
        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
        llist2_count = int(input())
        llist2 = SinglyLinkedList()
        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
        llist3 = mergeLists(llist1.head, llist2.head)
        print_singly_linked_list(llist3, " ", fptr)
        fptr.write("\n")

    fptr.close()
