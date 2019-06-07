from email import Menu, Customers

class UI_Menu:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            "1": self.show_customers,
            "2": self.add_new_customer,
            "3": self.edit_customer_info,
            "4": self.delete_customer_info,
            "5": exit
        }

    def display_menu(self):
        print(
"""~~~Komodo Email Targeting~~~
1. See All Customers
2. Add New Customer
3. Edit Customer Info
4. Delete Customer
5. Exit
"""
)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option \n")
            action = self.choices.get(choice)
            if action: 
                action()
            else:
                print(f"{choice} Is Not A Valid Option")

    def show_customers(self):
        current_menu = self.menu.get_customers()
        for p in current_menu:
            print(p)

    def add_new_customer(self):
        i_fname = input("What Is The Customer's First Name? ")
        i_lname = input("What Is The Customer's Last Name? ")
        i_ctype = input("What Kind of Customer Is This (Past, Current, Potential? ").lower()

        self.menu.new_customers(i_fname, i_lname, i_ctype)


    def edit_customer_info(self):
        customers_id = int(input("Which Customer's Info Would You Like to Update? "))
        for customer in self.menu.get_customers():
            if customers_id == customer.id:
                update_fname = input("Update First Name: ")
                update_lname = input("Update Last Name: ")
                update_ctype = input("Update Customer Type (Past, Current, Potential): ").lower()
                customer = Customers(update_fname, update_lname, update_ctype)
                print("Customer Has Been Updated")
                break
        else:
            print("No Costumer With No ID Found")


    def delete_customer_info(self):
        delete_id = int(input("Which Customer Would You like To Delete? "))
        resp = self.menu.delete_customer(delete_id)
        if resp:
            print("Customer & Their Info Was Deleted")
        else:
            print("Invalid! No Matching IDs Were Found")


if __name__ == "__main__":
    UI_Menu().run()
