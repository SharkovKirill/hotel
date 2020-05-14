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
        return self.name
    def __repr__(self):
        return self.__str__()

#degree_of_comfort = {"стандарт" : 1, "стандарт_улучшенный" : 1.2, "апартамент" : 1.5}

clients = []
with open('booking.txt', 'r', encoding='utf-8') as booking:
    for line in booking.readlines():
        client = line.split()
        clients.append(Client(client))
print(clients)

'''
Kirill - vvod
Vova,Nikita - proverka
Sveta - print, PEP8
'''