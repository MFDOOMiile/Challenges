from claims import Menu

class UI_Menu:
    def __init__(self):
        self.menu = Menu()
        self.choices = {
            "1": self.all_claims,
            "2": self.next_claim,
            "3": self.new,
            "4": exit
        }

    def display_menu(self):
        print(
"""~~~Komodo Insurance Claim~~~
1. See All Claims
2. Take Care of Next Claim
3. Enter a New Claim
4. Exit
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

    def all_claims(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Claim ID   Claim Type     Date of Claim    Claim Reported   Valid     Amount     Description")
        current_menu = self.menu.get_claims()
        for item in current_menu:
            print(item)

    def next_claim(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if not self.menu.claims[0].valid:
            print("Claim ID   Claim Type     Date of Claim    Claim Reported   Valid     Amount     Description")
            print(self.menu.claims[0])
            self.menu.claims.pop(0)
            print("Claim Was Not Valid. Claim Has Been Deleted From List")
            return 
        else:
            print("This Is the Next Claim to Process")
            print("Claim ID   Claim Type     Date of Claim    Claim Reported   Valid     Amount     Description")
            print(self.menu.claims[0])
            claim_answer = input("Would You Like to Process This Claim (Yes or No): ").lower()
            if claim_answer == 'yes':
                self.menu.claims.pop(0)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Claim Has Been Processed & Deleted From List")
            else:
                pass


    def new(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        iclaimid = input("Whats the Claim ID: ")
        iacc_type = input("What Kind of Claim Is It (Auto, Boat, Theft, Etc): ")
        idate_of_acc = input("When Did the Claim Occur: ")
        idate_of_claim = input("When Was the Claim Reported: ")
        ivalid = input("Is This Claim Valid (True or False): ")
        iamount = input("How Much Is the Claim: ")
        idescript = input("Describe the Claim: ")

        self.menu.new_claim(iclaimid, iacc_type, idate_of_acc, idate_of_claim, ivalid, iamount, idescript)

if __name__ == "__main__":
    UI_Menu().run()

