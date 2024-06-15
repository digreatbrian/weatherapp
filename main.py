from kivy.utils import get_hex_from_color
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from theme import DefaultTheme as Theme


class Main(MDBoxLayout):
	'''Main widget'''


class WeatherApp(MDApp):
	def build(self):
		self.main = Main()
		self.theme_cls.colors["Teal"] = {
			"200" : get_hex_from_color(Theme.primary_light_color),
			"500" : get_hex_from_color(Theme.primary_color),
			"700" : get_hex_from_color(Theme.primary_color),
		}	
		self.theme_cls.primary_palette = "Teal"
		self.theme_cls.material_style = "M3"
		return self.main


if __name__ == '__main__':
	app = WeatherApp()
	app.run()
