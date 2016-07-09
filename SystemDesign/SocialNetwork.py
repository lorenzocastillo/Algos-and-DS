"""
How would you design the data structures for a very large social network?
"""


class GUID:
    machines = 0
    users = 0

    @staticmethod
    def guid(obj_type):
        if obj_type is User:
            GUID.users += 1
            return GUID.users
        elif obj_type is Machine:
            GUID.machines += 1
            return GUID.machines
        else:
            raise Exception("Unsupported ID for type %s" % str(obj_type))


class Server:
    def __init__(self):
        self.machines = dict() #id to machine
        self.person_id_to_machine_id = dict() #person id to machine id

    def get_machine_id(self, id):
        if id not in self.machines:
            raise Exception("No such machine found")
        return self.machines[id]

    def get_machine_id_for_user(self, id):
        if id not in self.person_id_to_machine_id:
            raise Exception("Person doesn't belong to a machine")
        return self.person_id_to_machine_id[id]

    def get_person(self, id):
        machine_id = self.get_machine_id_for_user(id)
        machine = self.machines[machine_id]
        return machine.get_user(id)

    def add_user(self, user):
        machine_id = hash(user) % len(self.machines) + 1
        self.person_id_to_machine_id[user.id] = machine_id
        machine = self.machines[machine_id]
        machine.users[user.id] = user


class Machine:
    def __init__(self):
        self.id = GUID.guid(Machine)
        self.users = dict()

    def get_user(self, id):
        if id not in self.users:
            raise Exception("User %i not found in machine %i" % (id,self.id))
        return self.users[id]

    def __hash__(self):
        return self.id

    def __repr__(self):
        return "m%i" % self.id


class User:
    def __init__(self, name):
        self.id = GUID.guid(User)
        self.name = name
        self.friend_ids = list()

    def add_friend(self, id):
        if id not in self.friend_ids:
            self.friend_ids.append(id)

    def __hash__(self):
        return self.id

    def __repr__(self):
        return self.name


server = Server()


def create_machines(num):
    for _ in range(num):
        m = Machine()
        server.machines[m.id] = m


def create_users(names):
    for name in names:
        server.add_user(User(name))


def connect(id1, id2):
    a = server.get_person(id1)
    b = server.get_person(id2)
    a.add_friend(id2)
    b.add_friend(id1)

create_machines(3)
create_users(['Wade', 'LeBron', 'Durant', 'Westbrook', 'Kobe', 'Howard', 'Odom', 'Varejao'])
connect(1, 2)
connect(2, 8)
connect(3, 4)
connect(5, 7)
connect(5, 6)
connect(1, 7)


print(server.machines)
for _, machine in server.machines.items():
    print(machine)
    print("-" * 10)
    for user_id, user in machine.users.items():
        print(user_id, user)
        print("Friends: ")
        for friend_id in user.friend_ids:
            print(server.get_person(friend_id))
        print("-"*10)

