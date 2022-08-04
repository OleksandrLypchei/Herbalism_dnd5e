import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class MainScreen(Screen):
    pass

class SearchScreen(Screen):
    def searching(self):
        founded = Popup()
        founded.title = "You've found an ingredient"
        founded.size_hint = (.8, .5)
        founded.open()


class Herbalism(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SearchScreen(name='search'))
        return sm


if __name__ == '__main__':
    Herbalism().run()
