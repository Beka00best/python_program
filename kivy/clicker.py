from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "500")
Config.set("graphics", "height", "400")

from random import random

class ClickerProgramApp(App):
	def click(self, args):
		self.button.text = str(int(self.button.text) + 1)
		self.button.background_color = [
			random(),
			random(),
			random(),
			random()
		]
	def build(self):
		self.button = Button(
			text = "0",
			font_size = 48,
			background_color = [1,1,1,1],
			on_press = self.click
		)
		return self.button

if __name__ == '__main__':
	ClickerProgramApp().run()