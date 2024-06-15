"""Module for all the app theme"""
from kivy.metrics import sp
from kivy.metrics import dp


class Theme(object):
	'''Base class for making a theme'''
	name = None
	radius = dp(10)
	def __init__(self):
		if not self.name:
			raise ValueError("Improperly configured theme ,please specify the name first")


class LightTheme(Theme):
	name = 'light'
	#colors
	primary_color = [.5 ,0 , .6, 1]
	primary_light_color =  [.70 ,.24, .79, 1]
	primary_opp_color = [1 ,1 ,1 ,1]
	primary_text_color = [.5 ,0 , .6, 1]
	primary_opp_text_color = [1 ,1 ,1 ,1]
	
	secondary_color = [0 ,0 ,0 ,.5]
	secondary_light_color = [0 ,0 ,0 ,.15]
	secondary_opp_color =  [1 ,1 ,1 ,1]
	secondary_text_color = [0 ,0 ,0 ,.5]
	secondary_opp_text_color = [1,1,1,.5]
	
	tertiary_color = None
	tertiary_opp_color = None
	tertiary_text_color = None
	tertiary_opp_text_color = None

	success_color = [0 ,.7 ,.1 ,1]
	success_light_color = [0 ,.7 ,.1 ,.7]
	error_color = [.8 ,0 ,.1 ,1]

	#fonts
	font = 'fonts/montserrat-regular.ttf'
	font_family = 'Montserrat, sans-serif'
	font_small = sp(13)
	font_medium = sp(17)
	font_large = sp(20)
	font_larger = sp(24)
	
class DefaultTheme(LightTheme):
	pass
	