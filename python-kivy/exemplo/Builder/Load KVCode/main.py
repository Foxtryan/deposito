from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kvcode = """ 
BoxLayout:
	orientation: "vertical"
	Button:
		text: "Olá Mundo"
	Button:
		text: "Hello World"
"""

class HelloWorld(App):
	def build(self):
		return Builder.load_string(kvcode)

janela = HelloWorld()
janela.run()