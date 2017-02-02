#coding: utf-8
#author: Rafael "Foxtryan" Franco
#Date: 30/01/2017
#Last Update: 02/01/2017
#Versão 0.1

''' KIVY '''
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
''' Tabela '''
from master import *

class ShowMenu(Screen):
	def on_press_box(self):
		self.manager.current = 'telabox'
	def on_press_porta(self):
		self.manager.current = 'telaporta'
	def on_press_sair(self):
		janela.get_running_app().stop()

# Box
class TelaBox(Screen):
	def on_press_bt(self):
		txt_largura = self.ids.txt_largura.text
		self.manager.current = 'showresultado'
		if txt_largura != "":
			self.manager.get_screen('showresultado').lbl_resultado = "Box medindo: "+txt_largura+"m"
			largura = float(txt_largura)
			valor1, valor2, valor3 = CalculoBox.calculo(largura)
			self.manager.get_screen('showresultado').lbl_1 = str(("%.2f"%valor1))
			self.manager.get_screen('showresultado').lbl_2 = str(("%.2f"%valor2))
			self.manager.get_screen('showresultado').lbl_3 = str(("%.2f"%valor3))	
		else:
			self.manager.get_screen('showresultado').lbl_resultado = "Medida não informada"
		self.ids.txt_largura.text = ""


class CalculoBox:
	def calculo(largura, altura = 1.90):
		#medidas
		largura = largura
		altura = altura
		m2 = altura * (largura + 0.05)
		#Kit
		if largura < 1.20:
			kit = F1_120
		elif largura < 1.33:
			kit = F1_133
		elif largura < 1.50:
			kit = F1_150
		elif largura <=1.80:
			kit = F1_180
		else:
			kit = F1_180 + 20.00
		#Cálculo Acrilico
		valor1 = m2 * 138
		#Cálculo V.T Incolor
		valor2 = m2 * Box_Inc
		valor2 = (valor2+kit) * Box_Ganho
		#Cálculo V.T Fume		
		valor3 = m2 * Box_Fume
		valor3 = (valor3+kit) * Box_Ganho
		return valor1, valor2, valor3

# tela porta
class TelaPorta(Screen):
#	def __init__(self):
#		pass
	def on_press_a(self):
		pass
	def on_press_2(self):
		pass
	def on_press_4(self):
		pass

class CalculoPorta:
	def calculo(largura, altura = 2.10):
		pass

# Resultados
class ShowResultado(Screen):
	lbl_resultado = StringProperty('My label')
	lbl_1 = StringProperty('0.00')
	lbl_2 = StringProperty('0.00')
	lbl_3 = StringProperty('0.00')

	def on_press_bt(self):
		self.manager.current = 'showmenu'
		self.manager.get_screen('showresultado').lbl_1 = "0.00"
		self.manager.get_screen('showresultado').lbl_2 = "0.00"
		self.manager.get_screen('showresultado').lbl_3 = "0.00"

# Manager
class MyScreenManager(ScreenManager):
	pass
class MainApp(App):
	def build(self):
		return Builder.load_string(open('visual.kv', encoding='UTF-8').read())

janela = MainApp()
#janela.title = 'Sistema de Orçamento'
janela.run()
