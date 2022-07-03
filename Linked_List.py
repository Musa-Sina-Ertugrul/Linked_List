class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):

        if self.head == None:
            print("Empty linked list")

        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data)
            if not itr.next == None:
                llstr += "-->"
            itr = itr.next

        print(llstr)

    def pop_front(self):
        if self.head == None:
            raise Exception("Linked list is empty")
        self.head = self.head.next

    def push_back(self, data):

        if self.head == None:
            self.push_front(data)
        else:
            node = Node(data)
            itr = self.head
            while itr.next != None:
                itr = itr.next
                if itr.next == None:
                    itr.next = node
                    break

    def pop_back(self):
        if self.head == None:
            raise Exception("Linked list iğs empty")
        else:
            itr = self.head
            while itr.next != None:
                if itr.next.next == None:
                    itr.next = None
                    break
                itr = itr.next

    def lenght(self):
        if self.head == None:
            return 0
        else:
            count = 1
            itr = self.head
            while itr.next != None:
                count += 1
                itr = itr.next
            return count

    def add_after(self, index, data):
        node = Node(data)
        count = 0
        itr = self.head
        while count != index - 1:
            count += 1
            itr = itr.next
            if count == index - 1:
                node.next = itr.next
                itr.next = node
                break

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False


ll = Linked_list()
ll.push_front(89)
ll.push_front(56)
ll.push_front(11)
ll.pop_front()
ll.push_back(34)
ll.pop_back()
print(ll.lenght())
ll.add_after(2, 67)
print(ll.is_empty())
ll.print()
