'''Line chart graph for temperature changes'''
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy_garden.graph import Graph, MeshLinePlot, SmoothLinePlot
from kivy.clock import Clock


class WeatherChart(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=10)
        title_label = MDLabel(text="Temperature Chart", halign='center', font_style="H5")

        # Chart setup
        self.graph = Graph(xlabel='Time', ylabel='Temperature (°C)', x_ticks_minor=5,
                          y_ticks_minor=1, y_grid_label=True, x_grid_label=True, padding=5,
                          x_grid=True, y_grid=True, xmin=-0, xmax=5, ymin=20, ymax=35)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.graph.add_plot(self.plot)

        self.layout.add_widget(title_label)
        self.layout.add_widget(self.graph)
        self.add_widget(self.layout)

        # Initialize data and timer
        self.temperatures = [10, 4, 7]
        Clock.schedule_interval(self.update_chart, 5)  # Update every 5 seconds

    def update_chart(self, dt):
        # Fetch new temperature data here (replace with actual implementation)
        new_temp = 10  # Get the latest temperature reading

        # Data handling
        self.temperatures.append(new_temp)
        max_points = 10  # Maximum number of points to display
        if len(self.temperatures) > max_points:
            self.temperatures = self.temperatures[-max_points:]

        # Update plot points and x-axis limits
        x_values = range(len(self.temperatures))
        self.plot.points = [(x, y) for x, y in zip(x_values, self.temperatures)]
        self.graph.xmin = max(0, len(self.temperatures) - max_points)
        self.graph.xmax = len(self.temperatures) - 1

        # Refresh the graph
        self.graph._update_labels()
        #self.graph._update_y_labels()
