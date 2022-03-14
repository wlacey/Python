# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:04:13 2021

@author: Will
"""

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        # Check inidicies limits.
        if index < 0 or index >= self.length:
            return None
        # Need to return temp.
        temp = self.head
        # Will check if index is in first-half of DLL.
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        # Will check if index is in second-half of DLL.
        else:
            temp = self.tail
            # range(start, iterator, reverse)
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        while temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        temp = self.get(index)
        # Instead of using before and after variables, we can just use temp pointers.
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        # Now isolate the temp node.
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
        
# Driver Code
dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)
dll.print_list()
dll.remove(1)
dll.print_list()
