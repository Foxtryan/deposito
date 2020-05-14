import sqlite3

class Login(object):

	def __init__(self, database):
		self._db = database
		self._conn = sqlite3.connect(database)

	def Registrar(self, nome, telefone, endereco):
		self._conn.execute("""
		INSERT INTO Agenda (nome,telefone,endereco)
		VALUES (?, ?, ?)""", (nome, telefone, endereco))
		self._conn.commit()
		return True

	def BuscarTudo(self):
		cursor = self._conn.execute("SELECT * from Agenda")
		descricao = list()
		for linha in cursor: 
			pessoa = dict()
			for i, coluna in enumerate(linha):
				pessoa[cursor.description[i][0]] = coluna
			descricao.append(pessoa)
		return descricao

	def BuscarID(self, id):
		valores = self.BuscarTudo()
		for valor in valores:
			if valor['id'] == id:
				return valor

	def Delete(self, id):
		id = int(id)
		self._conn.execute("DELETE FROM Agenda WHERE id=?", (id,))
		self._conn.commit()
		return True