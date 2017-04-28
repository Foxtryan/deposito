import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, StringProperty

# Conexão com DataBase
con = sqlite3.connect('registro.db')
c = con.cursor()

# Só para ter uma formatação destacada
class Cabecalho(Label):
	pass

class Itens(Label):
	pass

# Tabela de exibicao
class Tabela(GridLayout):

	def __init__(self, **kwargs):
		super(Tabela, self).__init__(**kwargs)
		self.buscar_dados()
		self.exibir()


	def buscar_dados(self):
		# Forma o cabeçalho
		banco = [{'id':'ID','nome':'Nome','idade':'Idade'}]
		# Acrescenta itens do banco de dados
		for linha in c.execute('SELECT * FROM pessoas ORDER BY id'):
			banco.append({'id':str(linha[0]),'nome':str(linha[1]),'idade':str(linha[2])})
		self.data = banco

	
	def exibir(self):
		self.clear_widgets()
		for i in range(len(self.data)):
			if i < 1:
				linha = self.criar_cabecalho(i)
			else:
				linha = self.informacao(i)
			for item in linha:
				self.add_widget(item)

	# Preenche o cabeçalho
	def criar_cabecalho(self, i):
		coluna1 = Cabecalho(text=self.data[i]['id'])
		coluna2 = Cabecalho(text=self.data[i]['nome'])
		coluna3 = Cabecalho(text=self.data[i]['idade'])
		return [coluna1, coluna2, coluna3]

	# Preenche a tabela
	def informacao(self, i):
		coluna1 = Itens(text=self.data[i]['id'])
		coluna2 = Itens(text=self.data[i]['nome'])
		coluna3 = Itens(text=self.data[i]['idade'])
		return [coluna1, coluna2, coluna3]

class Botao(Button):
	def sair(self):
		# fecha conexão com db
		con.close()
		# encerra a aplicação
		App.get_running_app().stop()


class Aplicativo(App):
	pass


if __name__ == '__main__':
	Aplicativo().run()