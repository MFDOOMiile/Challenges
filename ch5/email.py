# For their current customers, they want to send an appreciation email, something that says this:
# "Thank you for your work with us. We appreciate your loyalty. Here's a coupon."

# For past customers, they want to send a note that says something like this:
# "It's been a long time since we've heard from you, we want you back".

# For potential customers who have never worked with Komodo, they want to send an email
# that simply states what deals Komodo is currently offering. It would be something like this:
# "We currently have the lowest rates on Helicopter Insurance!"


last_id = 0

class Customers:
    # fname = first name, lname = last name, ctype = customer type
    def __init__(self, fname, lname, ctype):
        global last_id
        last_id += 1
        self.id = last_id
        self.fname = fname
        self.lname = lname
        self.ctype = ctype
        self.email = self.choose_email()

    def __repr__(self):
        return (f"{self.id}  {self.fname}    {self.lname}   {self.ctype}   {self.email}")


    def choose_email(self):
        if self.ctype == "current":
            return "Thank you for spending yo moniez with us! We lovez moniez!! Here'z a coupon for 1%! Spend More! Kay Thankz!"
        elif self.ctype == "past":
            return "Yo!! You hasn't given us any of your moniez lately.. Da Faq! Please spend moniez on us! Kay Thankz!"
        elif self.ctype == "potential":
            return "YoOoOoOo What Up G?! We has good shiznitz!! Check our shiznitz out!! Spend moniez! Kay Thankz!"
        else:
            return "Invalid Customer Type"



    

class Menu:
    def __init__(self):
        self.customers = []

    def get_customers(self):
        return self.customers

    def new_customers(self, fname, lname, ctype):
        new_customers = Customers(fname, lname, ctype)
        self.customers.append(new_customers)

    def find_customer(self, customer_id):
        for i in self.customers:
            if int(i) == int(customer_id):
                return True
        return None

    def update_customer(self, customer_id, fname, lname, ctype):
        i = self.find_customer(customer_id)
        if i:
            i.customers = Customers 
            return True
        return False

    def delete_customer(self, customer_id):
        for d in self.customers:
            if d.id == customer_id:
                self.customers.remove(d)
                return True
        return False



