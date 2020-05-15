class Client:
    def __init__(self, line):
        self.book_date = line[0]
        self.surname = line[1]
        self.name = line[2]
        self.patr = line[3]
        self.num_per = line[4]
        self.arrival = line[5]
        self.num_days = line[6]
        self.max_price = line[7]

    def __str__(self):
        return self.name  # вместо name можно ставить, что нужно

    def __repr__(self):
        return self.__str__()


class Room:

    degree_of_comfort = {"стандарт": 1, "стандарт_улучшенный": 1.2, "апартамент": 1.5}
    room_type = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}

    def __init__(self, line, free=None):
        self.id = line[0]
        self.type = line[1]
        self.number_of_persons = line[2]
        self.comfort = line[3]
        self.price = Room.room_type[self.type] * Room.degree_of_comfort[self.comfort]
        self.free = free

    def

    def __str__(self):
        return self.id  # вместо id можно ставить, что нужно

    def __repr__(self):
        return self.__str__()


food_cost = {0: 'без питания', 280: 'завтрак', 1000: 'полупансион'}


clients = []
with open('booking.txt', 'r', encoding='utf-8') as booking:
    for line_p in booking.readlines():
        client = line_p.split()
        clients.append(Client(client))
# print(clients[1].__dict__)


rooms = []
with open('fund.txt', 'r', encoding='utf-8') as fund:
    for line_n in fund.readlines():
        room = line_n.split()
        rooms.append(Room(room))
# print(rooms[15].__dict__)  # пример как можно доставать инфу в виде словаря


# начало алгоритма подбора
filtered = []
for guest in clients:
    for room_ in rooms:
        if room_.number_of_persons == guest.num_per:
            filtered.append(room_)
prices = []
for max_pay in clients:
    for price_ in rooms:
        if price_.price <= max_pay.max_price:
            prices.append(price_)



'''
Kirill - vvod
Vova, Nikita - proverka
Sveta - print, PEP8
'''
