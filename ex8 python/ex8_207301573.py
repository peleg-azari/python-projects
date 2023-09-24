''' Exercise #8. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
class Room:
    def __init__(self, floor, number, guests, clean_level, rank, satisfaction=1.0):
        if isinstance(clean_level, int) == False:
            print("'The type of one of the attributes is wrong'")
        if isinstance(rank, int) == False:
            print("'The type of one of the attributes is wrong'")
        if satisfaction is not int and not float:
            print("'The type of one of the attributes is wrong'")
        if not 1 <= clean_level <= 10 or not 1 <= rank <= 3 or not 1 <= satisfaction <= 5:
            print("'The value of one of the attributes is wrong'")
        self.clean_level = int(clean_level)
        self.rank = rank
        self.satisfaction = float(round(satisfaction, 1))
        if len(guests) == 0:
            self.guests = ["empty"]
        else:
            self.guests = [name.lower() for name in guests]
        self.floor = floor
        self.number = number


    def __repr__(self):
        string_guests = ""
        for g in self.guests:
            string_guests += g +", "
        return f"floor: {self.floor}\nnumber: {self.number}\nguests: {string_guests[:-2]}\n" \
               f"clean_level: {self.clean_level}\n" \
               f"rank: {self.rank}\n" f"satisfaction: {self.satisfaction}"

    def is_occupied(self):
        if self.guests != ["empty"]:
            return True
        return False

    def can_clean(self):
        return True

    def clean(self):
        if self.can_clean() is True:
            self.clean_level = min(10, self.clean_level + self.rank)
            return self.clean_level
        else:
            print("'Room cannot be cleaned'")
            return -1

    def better_than(self, other):
        if not isinstance(other, Room) and issubclass(other, Room):
            print("'Other must be an instance of Room'")
            return -1
        else:
            return (self.rank, self.floor, self.clean_level) > (other.rank, other.floor, other.clean_level)

    def check_in(self, guests):
        if not self.is_occupied():
            self.guests = [name.lower() for name in guests]
            self.satisfaction = 1.0
        else:
            print("'Cannot check-in new guests to an occupied room'")
            return -1

    def check_out(self):
        if self.is_occupied() is True:
            self.guests = ["empty"]
        else:
            print("'Cannot check-out an empty room'")
            return -1


    def move_to(self, other):
        if self.is_occupied() is False:
            print("'Cannot move guests from an empty room'")
            return -1
        elif other.is_occupied is True:
            print("'Cannot move guests into an occupied room'")
            return -1
        else:
            other.check_in(self.guests)
            self.check_out()
            if other.better_than(self):
                other.satisfaction = min(5.0, self.satisfaction + 1.0)
            else:
                other.satisfaction = self.satisfaction



#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def __init__(self, floor, number, guests, clean_level, rank=1, satisfaction=1.0, clean_stock=0):
        super().__init__(floor, number, guests, clean_level, rank, satisfaction)
        self.clean_stock = clean_stock

    def __repr__(self):
        return super().__repr__()+f"\ntype: BudgetRoom \nclean_stock: {self.clean_stock}"

    def can_clean(self):
        if self.clean_stock > 0:
            return True
        return False

    def clean(self):
        super().clean()
        if self.can_clean():
            self.clean_stock = self.clean_stock -1
        else:
            return -1

    def check_in(self, guests):
        if not self.is_occupied():
            self.clean_stock = 0
        super().check_in(guests)


    def move_to(self, other):
        s = super().move_to(other)
        if s != -1 and isinstance(other, BudgetRoom):
            other.clean_stock = self.clean_stock
        else:
            return s

    def grant_clean(self):
        if self.is_occupied():
            self.clean_stock += 1
            self.satisfaction = min(5.0, self.satisfaction + 0.5)
        else:
            print("'Cannot grant an empty room'")
            return -1

    def grant_snack(self):
        if not self.is_occupied():
            print("'Cannot grant an empty room'")
            return -1
        else:
            self.satisfaction = min(5.0, self.satisfaction + 0.8)
            self.clean_level = max(1, self.clean_level -1)


class LegacyRoom(Room):
    def __init__(self, floor, number, guests, clean_level,
                 rank=2, satisfaction=1.0,
                 minibar_drinks=2, minibar_snacks=2):
        super().__init__(floor, number, guests, clean_level,
                 rank, satisfaction) # מה לעשות עם הערכים השונים?
        self.minibar_drinks = minibar_drinks
        self.minibar_snacks = minibar_snacks

    def __repr__(self):
        return super().__repr__()+f"\ntype: LegacyRoom \nminibar_drinks: {self.minibar_drinks} \n" \
                                    f"minibar_snacks: {self.minibar_snacks}"

    def can_clean(self):
        return True

    def check_in(self, guests):
        s = super().check_in(guests)
        if s != -1:
            self.minibar_drinks = 2
            self.minibar_snacks = 2
        else: return s

    def add_drinks(self, quantity):
        self.minibar_drinks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.2 * quantity)

    def add_snacks(self, quantity):
        self.minibar_snacks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.3 * quantity)
        self.clean_level = max(1, self.clean_level -1)




#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel():
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms


    def __repr__(self):
        number_of_BudgetRoom = 0
        number_of_LegacyRoom = 0
        other_room_types = 0
        number_of_occupied_rooms = 0
        for room in self.rooms:
            if room.is_occupied():
                number_of_occupied_rooms += 1
            if isinstance(room, BudgetRoom):
                number_of_BudgetRoom += 1
            if isinstance(room, LegacyRoom):
                number_of_LegacyRoom += 1
            if not isinstance(room, LegacyRoom) and not isinstance(room, BudgetRoom):
                other_room_types += 1
        return f"{self.name} hotel has:\n{number_of_BudgetRoom} BudgetRooms\n" \
               f"{number_of_LegacyRoom} LegacyRooms\n{other_room_types} other room types\n" \
               f"{number_of_occupied_rooms} occupied rooms"



    def check_in(self, guests, rank):
        for room in self.rooms:
            if room.guests == ["empty"] and rank == room.rank:
                room.check_in(guests)
                return room


    def check_out(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                room.check_out()
                return room

    def upgrade(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                g = room
                for room in self.rooms:
                    if room.better_than(g) is True:
                        s = g.move_to(room)
                        if s != -1:
                            return room








#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6),
             BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    h = Hotel("Dan", rooms)
    print(h.upgrade("Liat"))
    print(h.check_out("Ronen"))
    print(h.check_in(["Alice", "Wonder"], 2))
    print(h.check_in(["Alex"], 3))
    print(h)
    print(h.check_in(["Oded", "Shani"], 3))
    print(h.check_in(["Oded", "Shani"], 1))
    print(h.check_out("Liat"))
    print(h.check_out("Liat"))
    print(h)


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    test_hotel()

