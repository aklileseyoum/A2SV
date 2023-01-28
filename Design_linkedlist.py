class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        current_node = self.head
        idx = 0
        while idx < index and current_node.next :
            current_node = current_node.next
            idx += 1
        if idx != index or not current_node:
            return -1
        return current_node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        prev_index = 0
        current_node = self.head
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        while prev_index < index-1:
            current_node = current_node.next
            prev_index += 1

        
        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        current_node = self.head
        if index == 0:
            self.head = current_node.next
            return
        idx = 0
        while idx < index - 1:
            current_node = current_node.next
            idx += 1
        if current_node:
            if not current_node.next:
                current_node.next = None
            else:
                current_node.next = current_node.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
