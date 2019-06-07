last_id = 0

class MenuItem:
    def __init__(self, name, descrip, ingred, price):
        global last_id
        last_id += 1
        self.id = last_id
        self.name = name
        self.descrip = descrip
        self.ingred = ingred
        self.price = price

    def __repr__(self):
        return (f"{self.id}. {self.name} - {self.descrip}\n   Includes {self.ingred}\n   ${self.price}")


class Menu:
    def __init__(self):
        self.menuitems = []

    def get_menu_items(self):
        return self.menuitems

    def new_item(self, name, descrip, ingred, price):
        new_item = MenuItem(name, descrip, ingred, price)
        self.menuitems.append(new_item)

    def find_item(self, item_id):
        for menu in self.menuitems:
            if str(item_id) == str(item_id):
                return menu
        return None

    def update_item(self, item_id, item):
        item = self.find_item(item_id)
        if self.menuitems:
            self.menuitems.item = item
            return True
        return False

    def delete_item(self, item_id):
        for i in self.menuitems:
            if i.id == item_id:
                self.menuitems.remove(i)
                return True
        return False
    
    # mi = MenuItem("Hamburger", "Flame grilled patty on a pretzel bun \n", "Lettuce, tomato, cheese, onions, pickles, mayo \n", 5.25)
    # print(mi)
    

            




"""
    Each of their menu items will contain the following:
a meal number so employees can say "I'll have the #5",
a meal name,
a description,
a list of ingredients in the meal,
and a price.

Your task is to do the following:
1. Create a Menu class with constructors and instance attributes.
2. Create a MenuRepository class that has methods needed.
3. Create a Test Class for your repository methods. (You don't need to test
your constructors or objects. Just the methods.)
4. Create a User Interface file that allows the restaurant manager to add, delete,
and see all items in the menu list.
"""