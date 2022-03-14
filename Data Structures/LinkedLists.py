# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:17:55 2021

@author: Will
"""

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
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
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == None:
            return False
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend()
        if index == self.length:
            self.append()
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    def reverse(self):
        # Reverse head and tail.
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # Head and tail pointers are done but need the before and after variaables.
        # The steps for this must be exact.
        after = temp.next
        before = None
        # Iterate to reverse all pointers.
        for _ in range(self.length):
            after = temp.next
            # Reverses pointer.
            temp.next = before
            # Cannot break LL.
            before = temp
            temp = after
    
# Driver Code
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_list()
ll.reverse()
ll.print_list()
