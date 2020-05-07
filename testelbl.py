from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

kvcode = """

MeuLayout:
	orientation: 'vertical'

	Label: 
		id: lbl_um
		text: root.texto
		
	TextInput:
		id: txt_input
		hint_text: "Digite aqui."
		
	Button:
		text: "Alterar"
		on_press: root.clique(root.ids.txt_input.text)
		
"""

class MeuLayout(BoxLayout):
	'''
	Preparar texto inicial lbl_um, para vazio usar ""
	Comente a linha 31, tire o comentário da 32 e veja 
	a diferença do StringProperty
	'''
	texto = StringProperty("Texto inicial")
	#texto = 'INICIO'
	
	def clique(self, novo_texto):
		# Alterar lbl_um
		self.texto = novo_texto
		print(self.texto)

		
class Teste(App):
	def build(self):
		return Builder.load_string(kvcode)
		
if __name__ == '__main__':
	Teste().run()