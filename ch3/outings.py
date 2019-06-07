"""
Komodo accountants need a list of all outings, the cost of all outings combined, and the
cost of all types of outings combined.
Here are the parts of an outing:
	Event Type: Golf, Bowling, Amusement Park, Concert
	Number of people that attended,
	Date,
	Total cost per person for the event,
	Total cost for the event

Here's what they'd like:
1. Display a list of all outings.
2. Add individual outings to a list(don't need to worry about delete yet)
3. Calculations:
	They'd like to see a display for the combined cost for all outings.
	They'd like to see a display of outing costs by type.
		For example, all bowling outings for the year were $2000.00.
		All Concert outings cost $5000.00.
"""

last_id = 0

class Outings:
    def __init__(self, event, date, p_attend, pp_person):
        global last_id
        last_id += 1
        self.id = last_id
        self.event = event
        self.date = date
        self.p_attend = int(p_attend)
        self. pp_person = float(pp_person)
        self.tc_event = p_attend * pp_person

    def __repr__(self):
        return (f"{self.id}           {self.event}    {self.date}     {self.p_attend}            ${self.pp_person}               ${self.tc_event}")

class Menu:
    def __init__(self):
        self.outings = []

    def get_outings(self):
        return self.outings
    
    def type_list(self):
        pass
    
    def new_outing(self, event, date, p_attend, pp_person):
        new_outing = Outings(event, date, p_attend, pp_person)
        self.outings.append(new_outing)

        
    


# x = Outings("bowling", "11/11/11", 25, 20)
# print(x) 