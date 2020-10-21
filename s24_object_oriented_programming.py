class User:
    created_users = 0 # class attribute

    @classmethod
    def print_created_users(cls):
        print(User.created_users)

    @classmethod
    def from_string(cls, data_str):
        first, last = data_str.split(',')
        return cls(first, last)

    def __init__(self, first, last):
        self.first = first
        self.last = last
        User.created_users += 1

    def __repr__(self):
        return f"User: {self.full_name()}"
    
    def full_name(self):
        return f"{self.first} {self.last}"

class Pet:
    allowed = ('cat', 'dog', 'fish', 'rat')

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

User.print_created_users()

user1 = User("Jimi", "Hendrix")
print(user1.first, user1.last)
print(user1.full_name())

user2 = User("Joe", "Dalton")
print(user2.first, user2.last)

user3 = User.from_string("Steve,Vai")
print(user3) # calls __repr__

User.print_created_users()

p1 = Pet("Felix", "cat")
p2 = Pet("Tony", "tiger")