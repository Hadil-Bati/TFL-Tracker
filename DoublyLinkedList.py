class Node:
    def __init__(self,data, line):
        self.data = data # Station name
        self.next = None
        self.prev = None
        self.line = line # line
        self.links = {} # Every station linked to the node.
#Instances of the class 'Node' will be appended to the DLL.

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def next(self, cur = None):
        if cur is None:
            return
        cur = cur.next
        return cur

    def prev(self, cur = None):
        if cur is None:
            return
        cur = cur.prev
        return cur

    def append(self, data, line):
        if self.head == None:
            new_node = Node(data, line)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data, line)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            self.tail = new_node
# The function append will scroll through the list and if the list is empty it will append the element to the list straightaway
# and make it the head and tail of the list. If the list is not empty it will go through it until it reaches the end and then
# it will append the new element and make it the tail of the DLL.

    def search(self, station_to_search, line):
        cur = self.head
        while cur:
            if cur.data == station_to_search and cur.line == line:
                return cur
            else:
                cur = cur.next
# The function 'search' takes the name and the line of the station as parameters and returns the nodes that corresponds to that
# station. It is used by the function 'link_same_line' to add the next and previous station (on the same line) to each node in the DLL.

    def search_without_line(self, station):
        cur = self.head
        while cur:
            if cur.data == station:
                return cur
            else:
                cur = cur.next
        return None
# 'search without line' takes 'station' as parameter and returns any node with the same name.
# For example if the user inputs 'Waterloo' the function will look through the list and return the first node it finds
# with the same 'self.name' redardless of its line. It will return None if it can't find any node with the same name as
# the one passed to the function.