''' Exercise #8. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################

class Room:
    def __init__(self, floor, number, guests, clean_level, rank, satisfaction=1.0):
        if type(clean_level) != int or type(rank) != int or not isinstance(satisfaction, (float, int)):
            print("'The type of one of the attributes is wrong'")
        elif clean_level not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or rank not in [1, 2, 3] or satisfaction not in [float(i) for i in range(1,5)]:
            print("'The value of one of the attributes is wrong'")
        else:
            float_satisfaction = float(satisfaction)
            lower_guests = []
            if len(guests) == 0:
                lower_guests.append("empty")
            else:
                lower_guests = [word.lower() for word in guests]
            self.guests = lower_guests
            self.floor = floor
            self.number = number
            self.clean_level = clean_level
            self.rank = rank
            self.satisfaction = float_satisfaction

    def __repr__(self):
        str_guest =""
        for elem in self.guests[:-1]:
            str_guest += elem + ", "
        str_guest += self.guests[-1]
        return "floor: " + str(self.floor) + "\n" + "number: " + str(self.number) + "\n" + "guests: " + str_guest \
               + "\n" + "clean_level: " + str(self.clean_level) + '\n' + "rank: " + str(self.rank) + "\n" + "satisfaction: " + str(round(self.satisfaction, 1))

    def is_occupied(self):
        if self.guests[0] == "empty":
            return False
        return True

    def can_clean(self):
        return True

    def clean(self):
        if self.can_clean() is True:
            self.clean_level = min(10, self.clean_level + self.rank)
        else:
            print("'Room cannot be cleaned'")
            return -1


    def better_than(self, other):
        if not isinstance(other, (Room, LegacyRoom, BudgetRoom)):
           print("'Other must be an instance of Room'")
           return -1
        elif (self.rank, self.floor, self.clean_level) > \
                (other.rank, other.floor, other.clean_level):
            return True
        else:
            return False

    def check_in(self, guests):
        if self.is_occupied() is False:
            self.satisfaction = 1.0
            lower_guests = []
            for elem in guests:
                lower_guests.append(elem.lower())
            self.guests = lower_guests
        else:
            print("'Cannot check-in new guests to an occupied room'")
            return -1

    def check_out(self):
        if self.guests[0] == "empty":
            print("'cannot check-out an empty room'")
            return -1
        else:
            self.guests = ["empty"]

    def move_to(self, other):
        if self.guests[0] == "empty":
            print("'Cannot move guests from an empty room'")
            return -1
        elif other.guests[0] != "empty":
            print("'Cannot move guests into an occupied room'")
            return -1
        else:
            other.check_in(self.guests)
            self.check_out()
            if other.better_than(self) is True:
                other.satisfaction = min(5.0, self.satisfaction + 1.0)
            else:
                other.satisfaction = self.satisfaction

#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def __init__(self, floor, number, guests, clean_level,
                 rank=1, satisfaction=1.0, clean_stock=0):
        super().__init__(floor, number, guests, clean_level,
                 rank, satisfaction)
        self.clean_stock = clean_stock

    def __repr__(self):
        original = Room.__repr__(self)
        return original + "\n" + "type: BudgetRoom" +"\n" + "clean_stock: " + str(self.clean_stock)
    def can_clean(self):
        if self.clean_stock > 0:
            return True
        return False

    def clean(self):
        if self.can_clean() is True:
            Room.clean(self)
            self.clean_stock -= 1
        else:
            print("'Room cannot be cleaned'")
            return -1

    def check_in(self, guests):
        if self.is_occupied() is False:
            self.clean_stock = 0
        super().check_in(guests)

    def move_to(self, other):
        s = super().move_to(other)
        if s != -1 and type(other) == BudgetRoom:
            other.clean_stock = self.clean_stock
        else: return s

    def grant_clean(self):
        if self.is_occupied() is True:
            self.clean_stock += 1
            self.satisfaction = min(5.0, self.satisfaction + 0.5)
        else:
            print("'Cannot grant an empty room'")
            return -1

    def grant_snack(self):
        if self.is_occupied() is True:
            self.clean_level = max(1, self.clean_level - 1)
            self.satisfaction = min(5.0, self.satisfaction + 0.8)
        else:
            print("'Cannot grant an empty room'")
            return -1

class LegacyRoom(Room):
    def __init__(self, floor, number, guests, clean_level,
                 rank=2, satisfaction=1.0,
                 minibar_drinks=2, minibar_snacks=2):
        super().__init__(floor, number, guests, clean_level,
                 rank, satisfaction)
        self.minibar_drinks = minibar_drinks
        self.minibar_snacks = minibar_snacks

    def __repr__(self):
        original = Room.__repr__(self)
        return original + "\n" + "type: LegacyRoom" "\n" + "minibar_drinks: " +\
               str(self.minibar_drinks) + '\n' + "minibar_snacks: " + str(self.minibar_snacks)

    def check_in(self, guests):
        s = super().check_in(guests)
        if s != -1:
            self.minibar_snacks = 2
            self.minibar_drinks = 2
        else:
            return s

    def add_drinks(self,quantity):
        self.minibar_drinks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.2 * quantity)

    def add_snacks(self,quantity):
        self.minibar_snacks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.3 * quantity)
        self.clean_level = max(1, self.clean_level - 1)

#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    def __repr__(self):
        return self.name + "hotel has:" + '\n' + self.count_rooms()

    def count_rooms(self):
        LegacyRooms = BudgetRooms = other_rooms = occupied_rooms = 0
        for room in self.rooms:
            if type(room) is LegacyRoom:
                LegacyRooms += 1
            if type(room) is BudgetRoom:
                BudgetRooms += 1
            if not isinstance(room, (LegacyRoom, BudgetRoom)):
                other_rooms += 1
            if room.is_occupied() is True:
                occupied_rooms += 1
        return str(BudgetRooms) + " BudgetRooms" + "\n" + \
               str(LegacyRooms) + " LegacyRooms" + '\n' + str(other_rooms) + " other room types" + '\n'\
               + str(occupied_rooms) + " occupied rooms"

    def check_in(self, guests, rank):
        for room in self.rooms:
            if room.rank == rank and not room.is_occupied():
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
    # rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6), BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    # h = Hotel("Dan", rooms)
    # print(h.upgrade("Liat"))
    # print(h.check_out("Ronen"))
    # print(h.check_in(["Alice", "Wonder"], 2))
    # print(h.check_in(["Alex"], 3))
    # print(h)
    # print(h.check_in(["Oded", "Shani"], 3))
    # print(h.check_in(["Oded", "Shani"], 1))
    # print(h.check_out("Liat"))
    # print(h.check_out("Liat"))
    # print(h)
    r1 = Room(1, 1, ["Ted Mosby", "Barney Stinson", "Marshall Eriksen"], 4, 2, 3.7)
    print(r1)
    # r2 = Room(1, 2, [], 8, 3)
    # r3 = Room(1, 3, ["Hannah Horvath", "Marnie Michaels", "Jessa Johansson", "Shoshanna Shapiro"], 8, 1)
    # hotel = Hotel("Chanendler Bong Hotel", [r2, r3])
    # print(hotel)
    #########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    test_hotel()

