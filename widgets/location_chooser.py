'''Location selector widget'''
from xkivy.uix.dropdown import XDropDown
from theme import DefaultTheme as Theme


class LocationChooser(XDropDown):
	'''Location chooser dropdown'''
	
	def on_parent(self, *args):
		self.xradius = [Theme.radius] * 4
		self.option_xbg_color = Theme.primary_light_color
		self.values = [
			"Chinhoyi",
		    "Harare", 
		    "Bulawayo",
		    "Mutare",
		    "Gweru",
		    "Kwekwe",
		    "Kadoma",
		    "Masvingo",
		    "Chitungwiza",
		    "Marondera",
		    "Zvishavane",
		    "Redcliff",
		    "Beitbridge",
		    "Victoria Falls",
		    "Kariba",
		    "Hwange",
		    "Bindura",
		    "Chegutu",
		    "Norton",
		    "Rusape"
		]
		
	def on_option_release(self, ins):
		dashboard = self.parent.children[1].update_data(ins.text)
		