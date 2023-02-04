from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from widgets.notify import Notify
from widgets.popup import Pop
from widgets.button import FlatButton

class OtpScreen(MDScreen):
    Builder.load_file("views/otp.kv")

    ['null', 'text', 'number', 'url', 'mail', 'datetime', 'tel', 'address']
    def validate_otp(self, otp):
        otps = self.ids['otp_lbl'].text
        print(f"otps::: {otps}")
        print(f"otp::: {otp}")
        if otp != otps:
            Notify().notify("Otp is not correct", error=True)
            return "error"
        else:
            return "correct"