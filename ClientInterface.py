from Client import Client
from Sale import Sale
from Product import Product

from Inventory import Inventory

def listClients(inventory:Inventory):
    print("Listing clients")
    clients = inventory.getClients()
    for client in clients:
        print(client)

def addClient(inventory:Inventory):
    print("Adding new client")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    client = Client(0, name, email, phone)
    inventory.addClient(client)

def updateClient(inventory:Inventory):
    print("Updating client")
    id = input("Client ID: ")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    client = Client(id, name, email, phone)
    inventory.updateClient(client)

def deleteClient(inventory:Inventory):
    print("Deleting client")
    id = input("Client ID: ")
    inventory.deleteClient(id)

def printClientDetails(inventory:Inventory):
    print("Printing client details")
    id = input("Client ID: ")
    client = inventory.getClientById(id)
    print(client)
    print("Sales:")
    sales = inventory.getSalesByClient(id)
    for sale in sales:
        print(sale)
