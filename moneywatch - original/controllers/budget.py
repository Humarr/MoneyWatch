from time import sleep
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
# from controllers.home import HomeScreen
# from models.androidly import Sms
from models.database import DatabaseManager
# from kivy.app import App
from models.today import today_date

from widgets import notify
# from app.app import Moneywatch
# import re


class BudgetScreen(MDScreen):

    Builder.load_file("views/budget.kv")
    conn = DatabaseManager().conn
    cursor = conn.cursor()

    def format(self, budget):
        """
        The format function takes a number and inserts commas into it to make it more readable.
        For example, if you give format function the parameter 3145 it will return 3,145.

        :param self: Access variables that belongs to the class
        :param budget: Format the budget value to a more readable format
        :return: A formatted string from the input
        :doc-author: Trelent
        """

        # while True:
        if len(budget) > 3:
            budget = budget.replace(",", "")
            formatted_budget = (format(int(budget),  ',d'))
            print(formatted_budget)
            # self.ids['budget'].text = ""
            self.ids['budget'].text = formatted_budget

    def save_budget(self, budget):
        """
        The save_budget function saves the budget entered by the user to a database.
        It takes in one argument, budget and returns nothing.

        :param self: Access variables that belongs to the class
        :param budget: Store the budget entered by the user
        :return: None
        :doc-author: Trelent
        """

        email = self.manager.get_screen("login").ids['email'].text
        # sms = Sms().sms
        # print(sms)
        if budget == "":
            notify.Notify().notify("Enter your month's budget", error=True)
        else:
            sql = "INSERT INTO budget (email, budget, date) VALUES (?,?,?)"
            self.cursor.execute(sql, (email, budget, today_date))
            self.conn.commit()
            notify.Notify().notify("budget updated successfully")
            sleep(3)
            self.manager.current = "home"
            # Moneywatch().change_screen("home")
            # self.manager.switch_to(HomeScreen())
