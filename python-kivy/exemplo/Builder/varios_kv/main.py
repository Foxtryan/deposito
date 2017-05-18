from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class Tela1(Screen):
	pass

class Tela2(Screen):
	pass

class Aplicativo(App):

	def build(self):
		return Builder.load_file('tela1.kv')

Aplicativo().run()