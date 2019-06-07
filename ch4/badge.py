# 1. Create a dictionary of badges.
# 2. The key for the dictionary will be the BadgeID.
# 3. The value for the dictionary will be the List of Door Names.

# create a new badge
# update doors on an existing badge.
# delete all doors from an existing badge.
# show a list with all badge numbers and door access

# class Badges:
#     def __init__(self, badge_id, door_access):
#         self.badge_id = badge_id
#         self.door_access = door_access

#     def __repr__(self):
#         return f"{badge_id} {seldoor_access}"

    
class Menu:
    def __init__(self):
        self.badges = {}

    def get_badge(self):
        return self.badges

    def new_badge(self, badge_id, door_access):
        if badge_id in self.badges.keys():
            self.badges[badge_id].append(door_access)
        else:
            self.badges.update({badge_id:[door_access]})

    def find_badge(self, badge_id):
        for i in self.badges:
            if str(badge_id) == str(badge_id):
                return True
        return None

    def update_badge(self, badge_id, item):
        check = self.find_badge(badge_id)
        if check:
            for keys, values in self.badges.items():
                print(keys)
                if int(keys) == int(badge_id):
                    values.append(item)
                    self.badges.update({keys: values})
            return True
        return False

    def delete_badge(self, badge_id):
        for d in self.badges:
            if int(d) == int(badge_id):
                self.badges.pop(d)
                return True
        return False
