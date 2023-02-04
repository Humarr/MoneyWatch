from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ColorProperty, NumericProperty, StringProperty
# from kivy.clock import Clock
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import ThreeLineAvatarListItem, OneLineIconListItem
from kivy.uix.boxlayout import BoxLayout
from models.database import DatabaseManager

from widgets.popup import Pop


class CircularProgressBar(MDAnchorLayout):
    bar_color_bg = ColorProperty()
    bar_color = ColorProperty()
    set_value = NumericProperty()
    # percentage = StringProperty("0%")
    # duration = NumericProperty(1.5)
    # value = NumericProperty(45)
    # counter=0

    # def __init__(self, **kwargs):
    #     super(CircularProgressBar, self).__init__(**kwargs)
    #     Clock.Schedule_once(self.animate, 0)

    # def animate(self, *args):
    #     Clock.schedule_interval(self.counter_func, 1)

    # def counter_func(self, *args):
    #     if self.counter < self.value:
    #         self.counter+=1
    #     else:
    #         Clock.unschedule(self.counter_func)


class ExpenseList(ThreeLineAvatarListItem, MDFloatLayout, CommonElevationBehavior):
    # class ExpenseList(BaseListItem, MDFloatLayout, CommonElevationBehavior):
    # class ExpenseList(MDCard):
    # md_bg_color = [0, 0, 1, 1]
    category = StringProperty()
    icon = StringProperty()
    amount = StringProperty()
    date = StringProperty()
    item = StringProperty()


class Item(OneLineIconListItem):
    pass


class UpdateBudgetContent(BoxLayout):
    pass


class HomeScreen(MDScreen):
    Builder.load_file("views/home.kv")

    def info(self):
        """
        The info function displays the app's info in a popup.


        :param self: Access the attributes and methods of the class in python
        :return: The about_pop variable
        :doc-author: Trelent
        """

        # self.app_pop.open()

        # items = []
        # for year in years:
        items = [
            Item(text=" App", on_press=self.app_popup),
            Item(text="Developer", on_press=self.info_popup),
        ]
        self.about_pop = Pop(title="About...",
                             type="simple",
                             items=items,
                             )
        self.about_pop.open()

    def info_popup(self, obj):
        """
        The info_popup function is used to display the information about the developer of this app.
        It displays a popup with his contact details and links to his social media accounts.

        :param self: Access the attributes and methods of the class in python
        :param obj: Pass the object that triggered the callback
        :return: The information about the developer
        :doc-author: Trelent
        """

        builder = """
                    Umar Sa'ad is an android/desktop app and software developer who is committed to helping individuals and business owners build solutions to their problems.

                    He runs Nice guy's, a creative company that offers graphic design and software solutions.

                    [color=#b90000]email: Saaduumar42@gmail.com
                    phone/whatsapp: +2348090935863[/color]
                    """
        self.info_pop = Pop(title="The Developer", text=builder)
        self.about_pop.dismiss()
        self.info_pop.open()

    def app_popup(self, obj):
        """
        The app_popup function displays a popup window with information about the Money Watch app.


        :param self: Access the attributes and methods of the class in python
        :param obj: Pass the object that triggered the callback
        :return: The following:
        :doc-author: Trelent
        """

        self.about_pop.dismiss()
        the_app = """
                    Money watch app helps you keep track of all your expenses and helps you stick to your budget.

                    Your monthly income is entered and all your expenses are recorded. If you have spent an amount of money almost equal to your monthly income, Money watch infirms you so that you can make some necessary changes to your spending.
        """

        self.app_pop = Pop(title="Money Watch App", text=the_app)
        self.app_pop.open()
