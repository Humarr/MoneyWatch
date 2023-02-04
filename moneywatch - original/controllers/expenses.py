from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.properties import StringProperty
from models.database import DatabaseManager
from widgets.notify import Notify
from models.today import date_dict2, today_date
from models.popup_items import icons

class ExpenseList2(ThreeLineAvatarListItem, MDFloatLayout, CommonElevationBehavior):
    # class ExpenseList(BaseListItem, MDFloatLayout, CommonElevationBehavior):
    # class ExpenseList(MDCard):
    # md_bg_color = [0, 0, 1, 1]
    category = StringProperty()
    icon = StringProperty("food")
    amount = StringProperty()
    date = StringProperty()
    item = StringProperty()


class ExpensesScreen(MDScreen):
    Builder.load_file("views/expenses.kv")
    conn = DatabaseManager().conn
    cursor = conn.cursor()

    def search(self, search):
        """
        The search function is used to search for expenses in the database.
        It takes a string as an argument and searches through the database for that string.
        If found, it displays all the expenses with that particular string in them.
        
        :param self: Access variables that belongs to the class
        :param search: Search for the expense of a particular month
        :return: A list of widgets that have been added to the expense_container
        :doc-author: Trelent
        """
        
        """Fetches all the amount spent for the month from the database"""
        if search != "":
            search = search.strip()
            search=search.replace(" ", "")
            search = search.split(",")
            # print(date_dict2.keys())
            # print(date_dict2.values())
            keys = date_dict2.keys()
            # current = str(today_date).split("-")
            # month_year = f"{current[0]}-{current[1]}"
            for key in keys:
                # print(key)
                if key in search[0].title():
                    # break
                    month = date_dict2[f"{search[0][:3].title()}"]
                    try:
                        year = search[1]

                        print(month, year)
                        month_year = f"{year}-{month}"
                        print(month_year)

                        
                        email = self.manager.get_screen("login").ids['email'].text
                        sql = "SELECT * FROM expenses WHERE email=?"
                        # sql_expense = "SELECT price FROM expenses WHERE email=? AND strftime('%Y-%m', price) =?"
                        self.cursor.execute(sql, (email, ))
                        # global result
                        result = self.cursor.fetchall()
                        self.ids['expense_container'].clear_widgets()
                        print(f"expense_result: {result}")
                        if result:
                            # print(f"05: {result[0][5]}")
                            # print(f"05 2nd: {result[0][5][:7]}")
                            # price_list = []
                            # self.change_screen("home", switch=False)
                            self.ids['expense_container'].clear_widgets()
                            for value in result:
                                if month_year == value[5][:7]:
                                    # break
                                    # for price in result[0]:
                                    price = value[3]
                                    item = value[2]
                                    date = value[5]
                                    icon = value[4].lower()
                                    category = value[4].upper()

                                    self.ids['expense_container'].add_widget(ExpenseList2(
                                        category=category, icon=icons[icon], amount=price, date=date, item=item))
                                # break
                            else:
                                Notify().notify("No expenses in the specified month", error=True)
                            # price = sum(price_list)
                            # print(f"price_sum: {price}")
                            # return price

                        break
                    except IndexError:
                        Notify().notify("the month and year should be separated by ','", error=True)
            else:
                Notify().notify("must be in the form:: Month, Year", error=True)
        else:
            Notify().notify("Enter a search term...", error=True)

    def on_typing(self, search_text):
        self.ids['date_expense'].text = f"Expenses For {search_text.title()}"
