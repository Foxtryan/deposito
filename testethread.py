import threading
import time
import datetime
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder

kvcode = """

MeuLayout:
	orientation: 'vertical'
	Label:
		id: lbl_hora
		text: root.texto
		
	TextInput:
		id: txt_frase
		hint_text: "Digite 'pare' para parar a contagem"

	Button:
		text: "Enviar frase"
		on_press: root.cliquei(root.ids.txt_frase.text)

	Button:
		text: "Imprimir no console"
		on_press: print("Data atual: ",root.ids.lbl_hora.text)
"""

#status da thread
status = True

class MeuLayout(BoxLayout):

	texto = StringProperty("")
	global status

	def __init__(self, *args, **kwargs):

		super(MeuLayout, self).__init__(*args,**kwargs)
		self.iniciar_thread()

	def iniciar_thread(self):
		self.t = threading.Thread(target=self.relogio)
		self.t.start()

	def cliquei(self, texto):
		texto = texto.lower()
		if texto == 'pare':
			global status
			status = False
			print(texto)

	def relogio(self):
		while status == True:
			agora = datetime.datetime.now()
			agora = agora.strftime("%Y-%m-%d %H:%M:%S")
			self.update_ui(agora)
			time.sleep(1)

	def update_ui(self,agora):
		self.texto = str(agora)

class Aplicativo(App):
	def build(self):
		return Builder.load_string(kvcode)
		
if __name__ == '__main__':
	Aplicativo().run()
#fechar a execucao junto com programa
status = False