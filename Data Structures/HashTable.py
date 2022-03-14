class HashTable:
    
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ': ', val)
            
    def set_item(self, key, value):
        # First, find the address to store the pair.
        index = self.__hash(key)
        # Next, initialize the empty list at the "index" address.
        if self.data_map[index] == None:
            self.data_map[index] = []
        # Then, put the key-value pair in the address.
        self.data_map[index].append([key, value])
        
# Driver Code
ht = HashTable()
ht.set_item('bolts', 1400)
ht.set_item('washers', 500)
ht.set_item('lumber', 70)
ht.print_table()
