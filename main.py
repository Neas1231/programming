from kivy.config import Config
from kivy.app import App
from settings import Settings
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '680')

class Creator(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Settings()) # Настройки приложения
        layout.add_widget(Widget()) # Виджет для отступа
        return layout



if __name__ == '__main__':
    Creator().run()