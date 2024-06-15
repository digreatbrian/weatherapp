'''Dashboard for showing weather'''
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from utils.weather import get_weather_data
from theme import DefaultTheme as Theme
import multitasking
import requests


class WeatherDashboard(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)

        self.weather_card = MDCard(elevation=5)
        card_layout = MDBoxLayout(orientation='vertical', padding=15, spacing=10)
        self.location_label = MDLabel(text="Loading Location...", halign='center', font_style="H6")
        self.temp_label = MDLabel(text="--°C", halign='center', font_style="H2")
        self.condition_label = MDLabel(text="Loading...", halign='center')
        card_layout.add_widget(self.location_label)
        card_layout.add_widget(self.temp_label)
        card_layout.add_widget(self.condition_label)
        self.weather_card.add_widget(card_layout)
        self.layout.add_widget(self.weather_card)
        self.add_widget(self.layout)
        
        # update weather for the first time
        def update_weather(_):
        	location = self.parent.children[-1]
        	self.update_data(location=location.text)
        Clock.schedule_once(update_weather)
        self.description_map = {
		    200: ("Light thunderstorm with rain", "Light thunderstorm with rain, expect moderate rainfall and occasional lightning."),
		    201: ("Thunderstorm with rain", "Thunderstorm with rain, expect heavy rainfall and frequent lightning."),
		    202: ("Heavy thunderstorm with rain", "Heavy thunderstorm with intense rainfall, frequent lightning, and possible strong winds."),
		    210: ("Light thunderstorm", "Light thunderstorm with little or no rain, expect occasional lightning and thunder."),
		    211: ("Thunderstorm", "Thunderstorm with moderate lightning and thunder, may have light rainfall."),
		    212: ("Heavy thunderstorm", "Heavy thunderstorm with intense lightning and thunder, may have strong winds."),
		    221: ("Ragged thunderstorm", "Ragged thunderstorm with irregular lightning and thunder, potentially accompanied by rain."),
		    230: ("Thunderstorm with light drizzle", "Thunderstorm with light drizzle and occasional lightning."),
		    231: ("Thunderstorm with drizzle", "Thunderstorm with drizzle and frequent lightning."),
		    232: ("Thunderstorm with heavy drizzle", "Thunderstorm with heavy drizzle and intense lightning."),
		    300: ("Light drizzle", "Light drizzle, expect a fine mist of water droplets."),
		    301: ("Drizzle", "Drizzle, expect steady light rain."),
		    302: ("Heavy drizzle", "Heavy drizzle, expect continuous light rain."),
		    310: ("Light drizzle rain", "Light drizzle mixed with rain, expect a mix of mist and light rain."),
		    311: ("Drizzle rain", "Drizzle and rain, expect steady light to moderate rain."),
		    312: ("Heavy drizzle rain", "Heavy drizzle and rain, expect continuous moderate to heavy rain."),
		    313: ("Shower rain and drizzle", "Shower rain mixed with drizzle, expect intermittent rain showers."),
		    314: ("Heavy shower rain and drizzle", "Heavy shower rain mixed with drizzle, expect intense intermittent rain showers."),
		    321: ("Shower drizzle", "Shower drizzle, expect short bursts of light rain."),
		    500: ("Light rain", "Light rain, expect a steady light rainfall."),
		    501: ("Moderate rain", "Moderate rain, expect a steady moderate rainfall."),
		    502: ("Heavy rain", "Heavy rain, expect intense rainfall that may cause flooding."),
		    503: ("Very heavy rain", "Very heavy rain, expect prolonged intense rainfall that may cause significant flooding."),
		    504: ("Extreme rain", "Extreme rain, expect torrential downpours that can lead to severe flooding and damage."),
		    511: ("Freezing rain", "Freezing rain, expect rain that freezes on contact with cold surfaces, creating icy conditions."),
		    520: ("Light shower rain", "Light shower rain, expect brief periods of light rainfall."),
		    521: ("Shower rain", "Shower rain, expect intermittent moderate rainfall."),
		    522: ("Heavy shower rain", "Heavy shower rain, expect intermittent intense rainfall."),
		    531: ("Ragged shower rain", "Ragged shower rain, expect irregular rain showers with varying intensity."),
		    600: ("Light snow", "Light snow, expect a light snowfall with little accumulation."),
		    601: ("Snow", "Snow, expect moderate snowfall."),
		    602: ("Heavy snow", "Heavy snow, expect intense snowfall with significant accumulation."),
		    611: ("Sleet", "Sleet, expect a mix of rain and snow or partially melted snowflakes."),
		    612: ("Light shower sleet", "Light shower sleet, expect brief periods of sleet with little accumulation."),
		    613: ("Shower sleet", "Shower sleet, expect intermittent sleet with moderate accumulation."),
		    615: ("Light rain and snow", "Light rain and snow, expect a mix of light rain and snow."),
		    616: ("Rain and snow", "Rain and snow, expect a mix of rain and snow with varying intensity."),
		    620: ("Light shower snow", "Light shower snow, expect brief periods of light snow."),
		    621: ("Shower snow", "Shower snow, expect intermittent moderate snowfall."),
		    622: ("Heavy shower snow", "Heavy shower snow, expect intermittent intense snowfall."),
		    701: ("Mist", "Mist, expect a thin fog that reduces visibility."),
		    711: ("Smoke", "Smoke, expect a haze caused by smoke that reduces visibility."),
		    721: ("Haze", "Haze, expect reduced visibility due to atmospheric particles like dust or smoke."),
		    731: ("Sand/dust whirls", "Sand/dust whirls, expect swirling sand or dust raised by strong winds."),
		    741: ("Fog", "Fog, expect thick fog that significantly reduces visibility."),
		    751: ("Sand", "Sand, expect windblown sand that may reduce visibility."),
		    761: ("Dust", "Dust, expect windblown dust that may reduce visibility."),
		    762: ("Volcanic ash", "Volcanic ash, expect ash ejected from a volcano that can affect visibility and air quality."),
		    771: ("Squalls", "Squalls, expect sudden, strong gusts of wind often associated with thunderstorms."),
		    781: ("Tornado", "Tornado, expect a violently rotating column of air that extends from a thunderstorm to the ground."),
		    800: ("Clear sky", "Clear sky, expect a bright sunny day with no clouds."),
		    801: ("Few clouds", "Few clouds, expect a mostly clear sky with a few scattered clouds."),
		    802: ("Scattered clouds", "Scattered clouds, expect a partly cloudy sky with clouds covering less than half of the sky."),
		    803: ("Broken clouds", "Broken clouds, expect a mostly cloudy sky with some breaks in the clouds."),
		    804: ("Overcast clouds", "Overcast clouds, expect a completely cloudy sky with no breaks in the clouds.")
		}

    def on_parent(self, *_):
    	if hasattr(self, "scheduled_update"):
    		return
    	update_interval = 1800 # seconds/30 minutes
    	# location
    	location = self.parent.children[-1]
    	Clock.schedule_interval(lambda x: self.update_data(location=location.text), update_interval)
    	self.scheduled_update = True
    
    @multitasking.task
    def update_data(self, location=None):
    	'''Updates the location data'''
    	# fetch data
    	data_interpretation_error = False
    	data = None
    	self.location_label.text = "%s"%location
    	#self.condition_label.text = "Loading..."
    	#self.temp_label.text = "--°C"
    	if self.parent.bio:
    		self.parent.bio.text = "Updating weather data..."
    	try:
    		data = get_weather_data(location)
    	except Exception as e:
    		if self.parent.weather_image:
    			# setting image for a problem
    			Clock.schedule_once(lambda dt:setattr(self.parent.weather_image,'source', "problem.png"))
    			
    		if issubclass(requests.exceptions.BaseHTTPError, Exception):
	    		# connection problems
	    		self.temp_label.text = "--°C"
	    		self.condition_label.text = "Error, please check connection"
	    		self.condition_label.color = Theme.error_color
	    		self.parent.bio.text = "Error fetching weather data. Please make sure your device is connected to the internet."
	    		return
	    	# else any other interpretion error
	    	
    	if not data:
    		# No data received or error interpreting data received
    		if self.parent.weather_image:
    				# setting image for a problem
	    			Clock.schedule_once(lambda dt:setattr(self.parent.weather_image,'source', "problem.png"))
	    	self.temp_label.text = "--°C"
    		self.condition_label.text = "Error fetching data"
    		self.condition_label.color = Theme.error_color
    		self.parent.bio.text = "Error fetching data. This problem maybe be called by the API endpoint in transferring data to this application."
    		return
    	# setting image back to default weather image if it has been changed to no internet /connection problem image
    	if self.parent.weather_image:
    		Clock.schedule_once(lambda dt:setattr(self.parent.weather_image,'source', "cloudy.png"))
	    
	    # weather condition/situation
    	condition = "Temperature: %.1f °C \nHumidity levels: %d{p}\nPressure: %d hPa\nWind speed: %.2f m/s"%(data.get('temperature'), data.get('humidity'), data.get('pressure'), data.get("wind_speed"))
    	condition = condition.format(p='%')
    	
    	# updating widgets
    	self.location_label.text = location
    	self.condition_label.text = condition
    	self.condition_label.color = Theme.success_color
    	self.temp_label.text = "%.1f °C"%(data.get('temperature'))
    	x_id = data.get('id')
    	try:
    		title, description = self.description_map.get(x_id)
    		bio = "[b]%s[/b]\n\n%s"%(title, description)
    	except: pass
    	self.parent.bio.text = data.get("description") if not bio else bio
    	
        