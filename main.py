class Client:
    def __init__(self, line):
        self.reserve = line[0]
        self.surname = line[1]
        self.name = line[2]
        self.patr = line[3]
        self.numper = line[4]
        self.arrival = line[5]
        self.numdate = line[6]
        self.max_sum = line[7]

    def __str__(self):
        return self.name  # вместо name можно ставить, что нужно

    def __repr__(self):
        return self.__str__()


class Room:
    def __init__(self, line):
        self.id = line[0]
        self.type = line[1]
        self.number_of_persons = line[2]
        self.comfort = line[3]

    def __str__(self):
        return self.id  # вместо id можно ставить, что нужно

    def __repr__(self):
        return self.__str__()


comfort_factor = [1, 1.2, 1.5]
degree_of_comfort = {1: "стандарт", 1.2: "стандарт_улучшенный", 1.5: "апартамент"}

room_type = {'одноместный': 2900, 'Двухместный': 2300, 'Полулюкс': 3200, 'Люкс': 4100}

food_factor = [0, 280, 1000]
food_cost = {0: 'без питания', 280: 'завтрак', 1000: 'полупансион'}



clients = []
with open('booking.txt', 'r', encoding='utf-8') as booking:
    for line in booking.readlines():
        client = line.split()
        clients.append(Client(client))
print(clients[1].__dict__)

rooms = []
with open('fund.txt', 'r', encoding='utf-8') as fund:
    for line in fund.readlines():
        room = line.split()
        rooms.append(Room(room))
print(rooms[15].__dict__)  # пример как можно доставать инфу в виде словаря
'''
Kirill - vvod
Vova,Nikita - proverka
Sveta - print, PEP8
'''
