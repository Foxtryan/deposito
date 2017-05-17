# coding: utf-8
# Exemplo básico de SplitScreen com gerenciador ScreenManager
# Autor: Rafael Muller Franco

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class Principal(BoxLayout):
    pass
class Primeira(Screen):
    pass
class Segunda(Screen):
	pass
class Comparativo(Screen):
	pass

class TesteApp(App):
    def build(self):
        return Principal()

if __name__ == "__main__":
    TesteApp().run()
