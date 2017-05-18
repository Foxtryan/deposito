from kivy.app import App
from kivy.lang import Builder

class HelloWorld(App):
	def build(self):
		return Builder.load_string(open('arquivo.kv', encoding='utf-8').read())
		#return Builder.load_file("arquivo.kv")
		
janela = HelloWorld()
janela.run()