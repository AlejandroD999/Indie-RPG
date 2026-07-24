
'''
Idea so far: Make inventory a new screen.

1. Key pressed while in game: Opens inventory
jjj
2. Current screen (in app) is inventory. 
    - Inventory drawn and interacted to the right side of the window

3. Player does actions
    If action == QUIT KEY or ESC:
       switch screen to game 

'''

'''
dict_key: array
1 [item_object, item_object, item_object]
2 

'''

class Inventory:
    def __init__(self, width, height, row_len, total_slots):
        # item_name: quantity
        self.table = {}
        
        self.total_slots = total_slots
        self.row_len = row_len

        self.used_slots = 0 
        
        self.setup_slots()

    def setup_slots(self):
        pass 

    def add_item(self, item_name, quantity):
        # TODO Later make item an object -> item.name
        
        if item_name in self.table:
            self.table[item_name] += quantity
            return

        self.table[item_name] = quantity
        self.used_slots += 1
            
    def remove_item(self, item):
        pass

    def return_items(self):
        # Return in form of array or dict
        print("Total Slots:", self.total_slots)
        print("Used:", self.used_slots)
        
        for i in range(1, self.total_slots + 1):
            if i % 6 == 0:
                print()

            if i <= self.used_slots:
                print(1, end="")
            else:
                print(0, end="")

        print()

    def save_inventory(self):
        # Connect to db and dump
        pass
    def update(self):
        pass

    def draw(self):
        pass



