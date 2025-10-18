from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import configparser


class Settings(BoxLayout):

    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        vspath = VScodePath()
        browserpath = BrowserPath()
        self.add_widget(vspath)
        self.add_widget(browserpath)
        self.add_widget(ConfirmSettings(vspath, browserpath))


class PathChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(PathChooser, self).__init__(**kwargs)
    
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

        popup = Popup(title='Выберите путь к VScode...', content=content, size_hint=(0.9, 0.9))

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

class VScodePath(PathChooser):
    def __init__(self, **kwargs):
        super(VScodePath, self).__init__(**kwargs)

class BrowserPath(PathChooser):
    def __init__(self, **kwargs):
        super(BrowserPath, self).__init__(**kwargs)
        
        
class ConfirmSettings(BoxLayout):
    def __init__(self, vspath, browserpath, **kwargs):
        super(ConfirmSettings, self).__init__(**kwargs)
        self.vspath = vspath
        self.browserpath = browserpath
        
    def confirm(self):
        config = configparser.ConfigParser()

        config['Settings'] = {
            'VScode': self.vspath.ids.user_input.text,
            'Browser': self.browserpath.ids.user_input.text
        }
        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        config_read = configparser.ConfigParser()
        config_read.read('config.ini')

        value1 = config_read.get('Settings', 'VScode')
        value2 = config_read.get('Settings', 'Browser')

        print(f"Значение из секции 1: {value1}")
        print(f"Значение из секции 2: {value2}")
        print('klass')