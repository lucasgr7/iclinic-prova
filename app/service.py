
import time
from .models import Client
from .models import ClientRepository
        
def search_clients(input):
    timeStart = time.time()
    if(input != None):
        input = input.lower()
        search_clients = list(filter(lambda x: input in x[1].lower()[0:len(input)], ClientRepository.index_clients))
        idxs = set(map(lambda x: x[0], search_clients))
        results = get_client_by_index(idxs, input)
        print('query time: ' + str(time.time() - timeStart))
        return results
    return []


def get_client_by_index(list_indexes, input):
    if len(list_indexes) > 0:
        results = list(filter(lambda x: x.index in list_indexes, ClientRepository.clients))
        search_clients = list(filter(lambda x: input in x.name.lower()[0:len(input)], results))
        idx_search_clients = list(map(lambda x: x.index, search_clients))
        for r in results:
            if(not r.index in idx_search_clients):
                search_clients.append(r)
        return search_clients

