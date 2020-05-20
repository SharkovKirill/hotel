import datetime
import random


class Client:
    '''Customer class'''

    def __init__(self, line):
        '''Initialization method'''

        self.book_date = line[0]
        self.surname = line[1]
        self.name = line[2]
        self.patr = line[3]
        self.fullname = line[1] +' '+ line[2]+' ' + line[3]
        self.num_per = line[4]
        self.num_days = datetime.timedelta(days=int(line[6]))
        self.max_price = int(line[7])
        self.ar = line[5]
        self.num_d = line[6]

        #Str into datetime
        arrival = line[5].split('.')[::-1]
        for dt in range(len(arrival)):
            arrival[dt] = int(arrival[dt])
        arrival = datetime.datetime(arrival[0], arrival[1], arrival[2])

        self.arrival = arrival

    def __str__(self):
        '''String representation method'''

        return self.name

    def __repr__(self):
        '''Representation method'''

        return self.__str__()


class Room:
    '''Room class'''

    degree_of_comfort = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    room_type = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}

    def __init__(self, line):
        '''Initialization method'''

        self.id = line[0]
        self.type = line[1]
        self.number_of_persons = line[2]
        self.comfort = line[3]
        self.price = Room.room_type[self.type] * Room.degree_of_comfort[self.comfort]
        self.occupied = False
        self.food = 'без питания'

    def __str__(self):
        '''String representation method'''

        return self.id

    def __repr__(self):
        '''Representation method'''

        return self.__str__()

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price


food_cost = {'без питания': 0, 'завтрак': 280, 'полупансион': 1000}

#Open file with guests and send them to the list
clients = []
with open('booking.txt', 'r', encoding='utf-8') as booking:
    for line_p in booking.readlines():
        client = line_p.split()
        clients.append(Client(client))

#Open file with rooms and send them to the list
rooms = []
with open('fund.txt', 'r', encoding='utf-8') as fund:
    for line_n in fund.readlines():
        room = line_n.split()
        rooms.append(Room(room))


f_data = dict()

#Full scan
for guest in clients:
    filtered = []
    #Taking rooms
    for p_room in rooms:
        if not p_room.occupied or p_room.occupied <= guest.arrival:
            if p_room.number_of_persons == guest.num_per:
                if p_room.price <= guest.max_price:
                    filtered.append(p_room)

    #Taking rooms with discount 30%
    if len(filtered) == 0:
        for p_room in rooms:
            if not p_room.occupied or p_room.occupied <= guest.arrival:
                if p_room.number_of_persons <= guest.num_per:
                    if p_room.price * 0.7 <= guest.max_price:
                        filtered.append(p_room)


        #Add food price to the final cost (for dicount)
        filtered.sort(reverse=True)
        for rm in filtered:
            if guest.max_price - rm.price * 0.7 >= 1000:
                rm.price += 1000
                rm.food = 'полупансион'
            elif guest.max_price - rm.price * 0.7 >= 280:
                rm.price += 280
                rm.food = 'завтрак'

    # Add food price to the final cost
    filtered.sort(reverse=True)
    for rm in filtered:
        if guest.max_price - rm.price >= 1000:
            rm.price += 1000
            rm.food = 'полупансион'
        elif guest.max_price - rm.price >= 280:
            rm.price += 280
            rm.food = 'завтрак'

    #The opportunity to cancel the room
    profit = 0
    if len(filtered) != 0:
        filtered.sort(reverse=True)
        if random.random() >= 0.25:
            rm_id = filtered[0].id
            rm_food = filtered[0].food

            for s_rm in rooms:
                if s_rm.id == rm_id:
                    s_rm.occupied = guest.arrival + guest.num_days
                    break
            total_cost = rm.room_type[rm.type] + food_cost[rm_food]
            lst = [rm_id, rm_food, total_cost]
            f_data[guest.surname +' '+ guest.name +' '+ guest.patr] = lst

        else:
            rm_id = filtered[0].id
            rm_food = filtered[0].food

            for s_rm in rooms:
                if s_rm.id == rm_id:
                    s_rm.occupied = guest.arrival + guest.num_days
                    break
            total_cost = rm.room_type[rm.type] + food_cost[rm_food]
            lst = ['о',rm_id, rm_food, total_cost]
            f_data[guest.surname +' '+ guest.name +' '+ guest.patr] = lst #отказ
            continue


    else:
        f_data[guest.surname +' '+ guest.name +' '+ guest.patr] = 'не найдено'
        continue
print('konec')
for key in list(f_data.keys()):
    if f_data[key][0]!= 'о' and f_data[key][0]!= 'н':
        for guest in clients:
            for room in rooms:
                if guest.fullname == key and room.id == f_data[key][0]:
                    print('-' * 100)
                    print('Поступила заявка на бронирование: ')
                    print(f'{guest.book_date} {guest.fullname} {guest.num_per} {guest.ar} {guest.num_d} '
                          f'{guest.max_price}')
                    print('Найден: ')
                    print('номер', room.id, room.type, room.comfort, 'рассчитан на', room.number_of_persons, 'чел.',
                          'фактически', guest.num_per, 'чел.', f_data[key][1], 'стоимость', f_data[key][2])
                    print('Клиент согласен. Номер забронирован.')

    elif f_data[key][0] == 'н':
        for guest in clients:
            if guest.fullname == key:
                print('-' * 100)
                print('Поступила заявка на бронирование: ')
                print(f'{guest.book_date} {guest.fullname} {guest.num_per} {guest.ar} {guest.num_d} '
                          f'{guest.max_price}')
                print('Предложений по данному запросу нет. В бронировании отказано.')

    elif f_data[key][0] =='о':
        for guest in clients:
            for room in rooms:
                if guest.fullname == key and room.id == f_data[key][1]:
                    print('-' * 100)
                    print('Поступила заявка на бронирование: ')
                    print(f'{guest.book_date} {guest.fullname} {guest.num_per} {guest.ar} {guest.num_d} '
                          f'{guest.max_price}')
                    print('Найден: ')
                    print('номер', room.id, room.type, room.comfort, 'рассчитан на', room.number_of_persons, 'чел.',
                          'фактически', guest.num_per, 'чел.', f_data[key][2], 'стоимость', f_data[key][3])
                    print('Клиент отказался от варианта.')

print('=' * 100)


#print(profit)

