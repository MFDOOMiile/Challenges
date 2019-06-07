from outings import Menu

class UI_Menu:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            "1": self.new_event,
            "2": self.all_outings,
            "3": self.all_costs,
            "4": exit
        }

    def display_menu(self):
        print(
"""~~~Komodo Outing Expenses~~~
1. Add New Outing
2. See All Outings
3. See Cost of Outings
4. Exit
"""
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("What Would You Like To Do? ")
            action = self.choices.get(choice)
            if action: 
                action()
            else:
                print(f"{choice} is not a valid option")

    def new_event(self): 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ievent = input("What was the new outing? ")
        idate = input("When did the outing take place (mm/dd/yyyy)? ")
        ip_attend = int(input("How many people attended? "))
        ipp_attend = float(input("How much was the outing per person? "))

        self.menu.new_outing(ievent, idate, ip_attend, ipp_attend)

    def all_outings(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Event ID    Event      Event Date   Attendance    Price Per Person    Total Cost")
        current_menu = self.menu.get_outings()
        for item in current_menu:
            print(item)

    def all_costs(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        outing_cost = input("Would you like to see total cost by event type or all events (Type or All)? ").lower()
        if outing_cost == "type":
            for i in self.menu.outings:
                print("~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Cost of Outings by Type")
                print(i.event,"'s total cast was $",i.tc_event)

        elif outing_cost == "all":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~Total Cost of All Outings~~~")
            x = 0
            for tc in self.menu.outings:
                x += tc.tc_event
            print("$",x)

if __name__ == "__main__":
    UI_Menu().run() 

