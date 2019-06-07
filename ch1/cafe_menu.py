from cafe import Menu

class UI_Menu:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            "1": self.show_menu,
            "2": self.add_menu_item,
            "3": self.update_menu_item,
            "4": self.delete_menu_item,
            "5": exit
        }
    
    def display_menu(self):
        print(
"""~~Komodo Cafe Menu~~
1. Show Menu Items
2. Add New Menu Item
3. Update A Menu Item
4. Delete A Menu Item
5. Exit
"""
        )
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("What Would You Like to Do? ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid option")


    def show_menu(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        current_menu = self.menu.get_menu_items()
        for item in current_menu:
            print(item)

    def add_menu_item(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        iname = input("What Is the New Food: ")
        idec = input("Describe Your New Item: ")
        iingred = input("List the Ingredients: ")
        iprice = float(input("Set A Price: "))

        self.menu.new_item(iname, idec, iingred, iprice)

        
    
    def update_menu_item(self):
        pass
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # item_id = input("Enter Food Number You'd Like to Edit: ")
        

    
    def delete_menu_item(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        item_id = int(input("Which Food Would You Like to Delete: "))
        resp = self.menu.delete_item(item_id)
        if resp: 
            print("Your Food Item Was Removed")
        else:
            print("No Matching ID Found")
       

if __name__ == "__main__":
   UI_Menu().run()
            



    
# test_ui = UI_Menu()
# test_ui.add_menu_item()
# print(test_ui.menu.menuitems)

