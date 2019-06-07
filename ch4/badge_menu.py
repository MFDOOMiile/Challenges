from badge import Menu


class UI_Menu:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            "1": self.new, 
            "2": self.all, 
            "3": self.edit,
            "4": self.delete,
            "5": exit
        }

    def display_menu(self):
        print(
"""~~~Komoda Badge IDs & Access Doors~~~
1. Make a New Badge
2. See All Badges & Access Door(s)
3. Update Badges
4. Delete a Badge
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

    def new(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ibadge_id = input("What's the Badge's ID? > ")
        idoor_access = input("What Doors Can This Badge Access? >")

        self.menu.new_badge(ibadge_id, idoor_access)
        

    def all(self):
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("ID    Access Doors")
        current_menu = self.menu.get_badge()
        for keys, values in current_menu.items():
            print(f'{keys}     {values}')


    def edit(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        edit_badge = int(input("Enter the Badge ID You'd Like to Update: "))
        edit_door = input("What Doors Would You Like to Add to This Badge? ")
        if edit_door:
            result = self.menu.update_badge(edit_badge, edit_door)
        elif result == False:
            print("Failed to Update Badge")
        else:
            print("Badge Has Been Updated")


    def delete(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        badge_id = int(input("Which Badge Would You Like to Delete? "))
        resp = self.menu.delete_badge(badge_id)
        if resp:
            print("Badge Has Been Deleted")
        else:
            print("No Matching Badge ID was found")



if __name__ == "__main__":
    UI_Menu().run()

    