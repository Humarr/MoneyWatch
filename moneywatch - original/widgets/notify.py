from kivymd.toast import toast
from kivy.utils import platform
if platform != "android":
    from kivymd.uix.snackbar import Snackbar
else:
    from kivymd.uix.snackbar import MDSnackbar, MDSnackbarCloseButton
# from kivymd.uix.snackbar.snackbar import MDSnackbar
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.metrics import dp
from .label import Text
from .button import FlatButton

# def snackbar_close(*args):


class Notify:
    

    def notify(self, message, method="snack", error=False):
        """
        The notify function is used to display a message to the user.
        It takes two arguments:
            1) The message you want displayed, and
            2) The method you want it displayed.

        :param self: Access the class attributes and methods
        :param message: Display the message on the snackbar
        :param method: Specify the type of notification that will be displayed
        :param error: Determine whether the message is an error or not
        :return: The snackbar object
        :doc-author: Trelent
        """

        if method == "toast":
            toast(message)
        elif method == "snack":
            if platform == "android":
                self.snackbar = MDSnackbar(Text(text=message, text_color="white"),
                                           MDSnackbarCloseButton(
                    icon="close",
                    theme_icon_color="Custom",
                    icon_color="#8E353C",
                    _no_ripple_effect=True,
                    on_release=self.snackbar_close),
                    pos_hint={"center_x": 0.5},
                    size_hint_x=0.9,
                    md_bg_color="red" if error == True else "green",

                )
                self.snackbar.open()
            else:
                self.snackbar = Snackbar(text=message,
                                         pos_hint={"center_x": 0.5},
                                         size_hint_x=0.9,
                                         bg_color="red" if error == True else "green",

                                         )
                self.snackbar.open()
        elif method == "dialog":
            self.dialog = MDDialog(text=f"[color=#1f1f1f]{message}[/color]", buttons=[FlatButton(text="Okay", on_release=self.dialog_close)])
            self.dialog.open()

    def snackbar_close(self, *args):
        self.snackbar.dismiss()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)
