from kivy.app import App
from kivy.lang import Builder
from kivymd.button import MDIconButton, MDFlatButton
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivymd.menu import MDDropdownMenu
from kivy.properties import StringProperty

kvcode = """
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu

<MLabel@Label>:
	id: lbl
	text: app.texto
	color: 0,0,0,1

ScreenManager:
	TelaEmissor:

<TelaEmissor>:
	BoxLayout:
		id: telaemissor
		orientation: 'vertical'

		Label:
			text: "Testes"
			color: 0,0,0,1

		btnTipoVenda:
			id: MD_tipoVenda
			pos_hint: {"x": 0.04, "y": 0.5}
			on_press: root.btnTipoVenda.mostrarMenu(self)
			MLabel:

		Button:
			text: "RESET"

"""



def Dentro():
	App.get_running_app().texto = "Dentro do Estado"

def Fora():
	App.get_running_app().texto = "Fora do Estado"


	
class TelaEmissor(Screen):
	menu_tipoVenda = [
		{'viewclass': 'MDMenuItem', 'text': 'Dentro do Estado', 'on_press':Dentro},
		{'viewclass': 'MDMenuItem', 'text': 'Fora do Estado', 'on_press':Fora},
	]
	class btnTipoVenda(MDFlatButton):

		def __init__(self, **kwargs):
			super(TelaEmissor.btnTipoVenda, self).__init__(**kwargs)

		def mostrarMenu(self):
			menu = MDDropdownMenu()
			menu.items = menu_tipoVenda
			menu.width_mult = 4
			menu.open(self)

class Aplicativo(App):

	theme_cls = ThemeManager()
	texto = StringProperty("Tipo de Venda")
	def build(self):
		return Builder.load_string(kvcode)

Aplicativo().run()
