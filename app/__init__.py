import os
from flask import Flask
from flask_restplus import Api
from .models import ClientRepository, Client
import csv

# Initialize application
app = Flask(__name__)

with open('D:/GIT/iclinic/patients.csv', 'rt', encoding='utf8') as csvFile:
    spamreader = csv.reader(csvFile)
    index = 0
    clients = []
    index_clients = []
    for e in sorted(spamreader):
        clients.append(Client(e[0], index))
        for word in e[0].split(' '):
            index_clients.append((index, word))
        index += 1

    ClientRepository.clients = clients
    ClientRepository.index_clients = index_clients

from . import views

app.register_blueprint(views.bp)
api = Api(app)