class FileRepository:
	def __init__(self, fileName):
		self.fileName = fileName

	def getNextId(self):
		with open(self.fileName, "r") as f:
			lines = f.readlines()
			if len(lines) == 0:
				return 1
			else:
				lastLine = lines[-1]
				id = int(lastLine.split(",")[0])
				return id + 1

	def updateLine(self, id, data):
		with open(self.fileName, "r") as f:
			lines = f.readlines()
			for i in range(len(lines)):
				if int(lines[i].split(", ")[0]) == id:
					lines[i] = data + "\n"
					break
		with open(self.fileName, "w") as f:
			f.writelines(lines)

	def getAll(self): pass
	def saveAll(self, data): pass
	def add(self, data): pass
	def getById(self, id): pass
	def update(self, id, data): pass
	def delete(self, id): pass