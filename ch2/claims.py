"""\A Claim has the following properties:

ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid

Komodo allows an insurance claim to be made up to 30 days after an incident
took place.  If the claim is not in the proper time limit, it is not valid.

A ClaimType could be the following:
	Car, Home, Theft

The app will need methods in to do the following:
Show a claims agent a menu:

Choose a menu item:
1. See all claims
2. Take care of next claim
3. Enter a new claim

For #1, a claims agent could see all items in the queue listed out like this:

ClaimID   Type    Description             Amount      DateOfAccident  DateOfClaim      IsValid
1          Car    Car accident on 465.     $400.00     4/25/18         4/27/18          True
2          House  House fire in kitchen.   $4000.00    4/26/18         4/28/18          True
3          Theft  Stolen pancakes.         $4.00       4/27/18         6/01/18          False

1. Create a Claim class with constructors, class instances, and any necessary fields.
2. Create a ClaimRepository class that has proper methods.
3. Create a Test Class for your repository methods.
4. Create a Program file that allows a claims manager to manage items in a list of claims.
"""



class Claim:
    def __init__(self, claimid, acc_type, date_of_acc, date_of_claim, valid, amount, descript):
        self.claimid = claimid
        self.acc_type = acc_type
        self.descript = descript
        self.amount = amount
        self.date_of_acc = date_of_acc
        self.date_of_claim = date_of_claim
        if valid in ["false", "False"]:
            self.valid = False
        elif valid in ["true", "True"]:
            self.valid = True

    def __repr__(self):
        return f"{self.claimid}           {self.acc_type}            {self.date_of_acc}        {self.date_of_claim}         {self.valid}      ${self.amount}       {self.descript}"

class Menu:
    def __init__(self):
        self.claims = []

    def get_claims(self):
        return self.claims

    def new_claim(self, claimid, acc_type, date_of_acc, date_of_claim, valid, amount, descript):
        new_claim = Claim(claimid, acc_type, date_of_acc, date_of_claim, valid, amount, descript)
        self.claims.append(new_claim)


# x = Claim( 1, "Car", "03/09/1987", "03/12/1987", True, "4300", "T-Bone Rekt")
# print("Claim ID   Claim Type     Date of Claim     Claim Reported     Valid     Amount     Description")
# print(x)


