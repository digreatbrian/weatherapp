from kivy.metrics import sp, dp
from kivymd.uix.toolbar import MDTopAppBar
from xkivy.uix.label import XLabel
from widgets.menu import ToolbarMenu


class HeadlineLabel(XLabel):
	'''Label for toolbar headline'''
	def on_parent(self, *_):
		self.markup = True
		self.text = 'Best weather fetching tool'
		self.font_size = sp(14)

class Toolbar(MDTopAppBar):
	'''Main toolbar'''
	def __init__(self, *args, **kw):
		super().__init__(*args, **kw)
		self.menu = ToolbarMenu(None)
		
	def open_menu(self, instance):
		self.menu.caller = instance
		self.menu.open()
