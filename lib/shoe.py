#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int) and size > 0:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")

    def cobble_makes_new(self, brand, size, condition):
        self.brand = brand
        self.size = size
        self.condition = condition
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")


shoe = Shoe("Adidas", 9)