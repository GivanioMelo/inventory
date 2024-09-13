from Contact import Contact

class Client(Contact):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone)

    def fromString(string):
        id, name, email, phone = string.split(",")
        return Client(id, name, email, phone)

    def __str__(self):
        return f"{self.id},{self.name},{self.email},{self.phone}"

    def __repr__(self):
        return f"{self.id},{self.name},{self.email},{self.phone}"

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.id, self.name, self.email, self.phone)