class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1    
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True  
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length=-1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index <0 or index > self.length:
            return False
        if index == 0:
            self.length-=1
            return self.pop_first()
        if index == self.length-1:
            self.length-=1
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length-=1
        return True 
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def partition_list(self,x):
        if not self.head:
            return None
        dummy1=Node(0)
        dummy2=Node(0)
        prev1=dummy1
        prev2=dummy2
        current=self.head
        while current:
            if current.value<x:
                prev1.next = current
                prev1=current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev1.next=dummy2.next
        prev2.next=None
        self.head=dummy1.next
    
    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
    
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        for i in range(start_index):
            previous_node = previous_node.next
    
        current_node = previous_node.next
    
        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
    
        self.head = dummy_node.next

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        first = self.head
    
        while first and first.next:
            second = first.next
    
            # Perform the swap
            previous.next = second
            first.next = second.next
            second.next = first
    
            # Move pointers
            previous = first
            first = first.next
    
        self.head = dummy.next


    

    


def kth_node(ll,k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    return slow
        
        

        

my_linked_list = LinkedList(1)
my_linked_list.append(4)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(5)
print('Linked List before changing:')
my_linked_list.print_list()
print('Linked List after changing:')
my_linked_list.swap_pairs()
my_linked_list.print_list()




