from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class LoadingScreen(MDScreen):
    Builder.load_file("views/loading.kv")
    pass