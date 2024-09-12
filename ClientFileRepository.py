from Client import Client
from FileRepository import FileRepository

class ClientFileRepository(FileRepository):
	def __init__(self, fileName):
		super().__init__(fileName)

	def getAll(self):
		clients = []
		with open(self.fileName, "r") as f:
			for line in f:
				clients.append(Client.fromString(line))
		return clients

	def getAll(self):
		clients = []
		with open(self.fileName, "r") as f:
			for line in f:
				clients.append(Client.fromString(line))
		return clients

	def saveAll(self, clients):
		with open(self.fileName, "w") as f:
			for client in clients:
				f.write(str(client) + "\n")

	def add(self, client):
		client.id = self.getNextId()
		with open(self.fileName, "a") as f:
			f.write(str(client) + "\n")

	def getById(self, id):
		clients = self.getAll()
		for client in clients:
			if client.id == id:
				return client
		return None

	def update(self, client):
		self.updateLine(client.id, str(client))

	def delete(self, id):
		clients = self.getAll()