from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tela(BoxLayout):
	pass

class HelloWorld(App):
	def build(self):
		return Tela()

janela = HelloWorld()
janela.run()