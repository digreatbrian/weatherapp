from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from xkivy.properties import StringProperty
from theme import DefaultTheme as Theme
import webbrowser


class IconListItem(OneLineIconListItem):
	'''OneLineListItem with icon support'''
	icon = StringProperty("")
	def __init__(self, *a, **kw):
		super().__init__(*a, **kw)
		self.icon_widget = IconLeftWidget()
		self.add_widget(self.icon_widget)
		
	def on_icon(self, instance, icon):
		self.icon_widget.icon = icon


class ToolbarMenu(MDDropdownMenu):
	'''ToolBar Menu for Main Widget'''
	def __init__(self, caller, **kwargs):
		super().__init__(**kwargs)
		self.caller = caller
		self.width_mult = dp(76)
		# Setting menu items
		self.items = [
			{
				'viewclass':'IconListItem',
				'text':'Visit my Github',
				'theme_text_color': 'Custom',
				'text_color': Theme.primary_light_color,
				'icon': 'github',
				'on_release': lambda: webbrowser.open('https://github.com/digreatbrian')
			},
			{
				'viewclass':'IconListItem',
				'text':'Follow me',
				'icon': 'facebook',
				'theme_text_color': 'Custom',
				'text_color': Theme.primary_light_color,
				'on_release': lambda: webbrowser.open('https://facebook.com/digreatbrian')
			},
			{
				'viewclass':'OneLineListItem',
				'text':'[sub]By[/sub] Brian Musakwa',
				'theme_text_color': 'Custom',
				'text_color': Theme.primary_light_color,
				'opacity': .7,
			},
		]