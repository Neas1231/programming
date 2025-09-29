from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
    
class Settings(BoxLayout):

    def __init__(self):
        super(Settings, self).__init__()

    def select_path(self):
        content = BoxLayout(orientation='vertical')
        chooser = FileChooserListView(path='.', size_hint=(1, 0.9))
        chooser.multiselect = False
        chooser.dirselect = False
        btn_box = BoxLayout(size_hint=(1, 0.1))
        select_btn = Button(text='Выбрать')
        cancel_btn = Button(text='Отмена')
        btn_box.add_widget(select_btn)
        btn_box.add_widget(cancel_btn)
        content.add_widget(chooser)
        content.add_widget(btn_box)

        popup = Popup(title='Выберите путь', content=content, size_hint=(0.9, 0.9))

        def do_select(instance):
            selection = chooser.selection
            if selection:
                chosen = selection[0]
                # если выбрали директорию через dirselect, chooser.selection возвращает путь
                self.ids.user_input.text = chosen
            else:
                # нет выбора — можно взять текущую папку
                self.ids.user_input.text = chooser.path
            popup.dismiss()

        def do_cancel(instance):
            popup.dismiss()

        select_btn.bind(on_release=do_select)
        cancel_btn.bind(on_release=do_cancel)
        popup.open()

class Creator(App):

    def build(self):
        return Settings()


if __name__ == '__main__':
    Creator().run()