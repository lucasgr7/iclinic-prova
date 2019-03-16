class Client(object):
    name = ""
    index = 0

    def __init__(self, name, index):
        self.name = name
        self.index = index

class ClientRepository(object):
    
    clients = []
    index_clients = []
    def __init__(self, clients):
        self.clients = clients;
    
    def findAllClients(self):
        return self.clients

    def findAllIndexes(self):
        return self.index_clients