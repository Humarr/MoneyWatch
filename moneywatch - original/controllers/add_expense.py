from time import sleep
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from controllers.home import ExpenseList
from models.androidly import Storage
from models.database import DatabaseManager
from models.today import today_date
from models.popup_items import items, icons
from widgets import notify
from widgets.popup import Pop
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore


class Items(OneLineIconListItem):
    text = StringProperty()
    icon = StringProperty()


class AddExpenseScreen(MDScreen):
    Builder.load_file("views/add_expense.kv")
    conn = DatabaseManager().conn
    cursor = conn.cursor()
    path = Storage().storage()
    amount = JsonStore(f"{path}/expenses.json")
    current = str(today_date).split("-")
    month_year = f"{current[0]}-{current[1]}"
    def format(self, expense):
        """
        The format function takes a number (expense) as an argument and returns it with comma separators.
        For example: format(123456789, ',') will return 1,234,56789

        :param self: Access variables that belongs to the class
        :param expense: Store the value of expense that is entered by the user
        :return: The formatted string of the input number
        :doc-author: Trelent
        """

        # while True:
        if len(expense) > 3:
            expense = expense.replace(",", "")
            formatted_expense = (format(int(expense),  ',d'))
            print(formatted_expense)
            # self.ids['expense'].text = ""
            self.ids['price'].text = formatted_expense




    def categories(self, *instance):
        """
        The categories function creates a list of items that can be selected from.
        The items are displayed in a popup and when an item is selected, the function
        returns the text of the item. This text is then used to update the category field.

        :param self: Access variables that belongs to the class
        :param *instance: Pass the instance of the widget that called this function
        :return: A list of items that are assigned to the categories
        :doc-author: Trelent
        """

        items_list = []
        # items=items
        # print(f"inst: {instance}")
        for icon, category in items.items():
            items_list.append(
                Items(text=category, icon=icon, on_press=self.show_category_in_field))

        self.categories_pop = Pop(title="Categories...",
                                  type="simple",
                                  items=items_list,
                                  )
        self.categories_pop.open()

    def show_category_in_field(self, instance):
        """
        The show_category_in_field function is used to set the text of the category field to whatever was selected in the categories_popup.


        :param self: Access the attributes and methods of the class
        :param instance: Get the text from the button that was clicked
        :return: The category that was selected in the categories_popup
        :doc-author: Trelent
        """

        # print(obj)
        # self.close_categories_list()
        self.categories_pop.dismiss(force=True)
        Clock.schedule_once(lambda x : self.show(instance))
        
    def show(self, instance):
        # print(f"inst ::: {instance}")
        # instance.bg_color = "#e0ffff"
        self.ids['category'].text = instance.text.title()
        self.categories_pop.dismiss(force=True)
        # print(self.categories_pop.on_dismiss())
        # print("dismissed")
        # sleep(2)

    def dis(self, obj):
        print(obj)
        self.categories_pop.dismiss(force=True)

    def close_categories_list(self, *args):
        """
        The close_categories_list function closes the categories list when called.


        :param self: Access the attributes and methods of the class in python
        :param *args: Pass a variable number of arguments to a function
        :return: The categories_pop
        :doc-author: Trelent
        """

        self.categories_pop.dismiss(force=True)
