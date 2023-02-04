import math
import random

# from kaki.app import App
from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import CardTransition, ScreenManager
from kivy.utils import QueryDict, platform, rgba, hex_colormap
from kivymd.app import MDApp
# from kivymd.app import MDApp
# from PIL import ImageGrab

# from kivy.properties import ListProperty
from controllers.home import ExpenseList, UpdateBudgetContent
from models.androidly import Storage
from models.database import DatabaseManager
from models.popup_items import icons
from models.send_mail import send_email
from models.today import date_dict, today_date
# from controllers.splash import SplashScreen
from widgets import notify
from widgets.button import FlatButton, RoundButton
from widgets.popup import Pop

# TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size

# if platform == "linux" or platform == "win" or platform == "macosx":
#     Window.size = (350, 690)
#     Window.top = 0
#     Window.left = resolution[0] - Window.width
# Window.size = (350, 600)

# @mainthread


class WindowManager(ScreenManager):
    pass


class Moneywatch(MDApp):
    # class Moneywatch(MDApp, App):
    DEBUG = 1  # To enable Hot Reload
    CLASSES = {
        "HomeScreen": "controllers.home.HomeScreen",
        "SplashScreen": "controllers.splash.SplashScreen",
        "LoginScreen": "controllers.login.LoginScreen",
        "SignupScreen": "controllers.signup.SignupScreen",
        "ForgotScreen": "controllers.forgot.ForgotScreen",
        "BudgetScreen": "controllers.budget.BudgetScreen",
        "AddExpenseScreen": "controllers.add_expense.AddExpenseScreen",
        "ExpensesScreen": "controllers.expenses.ExpensesScreen",
        "OtpScreen": "controllers.otp.OtpScreen",
        "UpdateScreen": "controllers.update.UpdateScreen",
        "LoadingScreen": "controllers.loading.LoadingScreen",
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    KV_FILES = [
        "views/home.kv",
        "views/splash.kv",
        "views/login.kv",
        "views/signup.kv",
        "views/forgot.kv",
        "views/budget.kv",
        "views/add_expense.kv",
        "views/expenses.kv",
        "views/otp.kv",
        "views/update.kv",
        "views/loading.kv",
    ]

    # path = Storage().storage()
    # print(path)
    # # self.credentials = JsonStore(f"{self.path}/credentials.json")
    # screens_store = JsonStore(f"models/screens.json")
    # amount_store = JsonStore(f"amounts.json")
    # # screens_store = JsonStore(f"{path}/screens.json")
    # screen_history = ListProperty()
    colors = QueryDict()

    colors.primary = rgba("#143EBE")
    colors.bg = rgba("#1f1f1f")
    # colors.secondary = hex_colormap['steelblue']
    colors.secondary = hex_colormap['darkolivegreen']
    # colors.secondary = hex_colormap['chocolate']
    # colors.secondary = rgba("#492b7c")
    colors.warning = rgba("#c83416")
    colors.danger = hex_colormap['orangered']
    # colors.danger = rgba("#b90000")
    colors.success = hex_colormap['darkolivegreen']
    colors.white = rgba("#FFFFFF")
    colors.yellow = rgba("#f6d912")
    # colors.success = hex_colormap['darkolivegreen']
    # colors.orange = hex_colormap['orangered']
    colors.orange = rgba("#ed8a0a")
    colors.black = rgba("#333333")
    colors.grey = rgba("#f1f1f1")

    fonts = QueryDict()
    fonts.heading = 'assets/fonts/Poppins-Bold.ttf'
    fonts.subheading = 'assets/fonts/Poppins-Regular.ttf'
    fonts.body = 'assets/fonts/Poppins-Medium.ttf'

    fonts.size = QueryDict()
    fonts.size.heading = sp(30)
    fonts.size.icon = sp(30)
    fonts.size.h1 = sp(24)
    fonts.size.h2 = sp(22)
    fonts.size.h3 = sp(18)
    fonts.size.h4 = sp(16)
    fonts.size.h5 = sp(14)
    fonts.size.h6 = sp(12)
    fonts.size.h7 = sp(5)
    fonts.size.bar = sp(3)

    images = QueryDict()

    # current = str(today_date).split("-")
    # month_year = f"{current[0]}-{current[1]}"

    # # DatabaseManager().build_tables()
    # conn = DatabaseManager().conn
    # cursor = conn.cursor()

    def __init__(self, **kwargs):
        """
        The __init__ function is called when an instance of a class is created.
        It can be used to set up variables and attributes that the object will use later on.


        :param self: Refer to the current instance of the class
        :param **kwargs: Pass a keyworded, variable-length argument list
        :return: None
        :doc-author: Trelent
        """

        super().__init__(**kwargs)
        self.wm = WindowManager()
        self.path = Storage().storage()
        print(self.path)
        self.screens_store = JsonStore(f"models/screens.json")
        print(f"screen_store:: {self.screens_store}")
        self.screen_history = []
        # self.screen_history = ListProperty()

        self.amount_store = JsonStore(f"{self.path}/expenses.json")

        self.current = str(today_date).split("-")
        self.month_year = f"{self.current[0]}-{self.current[1]}"

        self.conn = DatabaseManager().conn
        self.cursor = self.conn.cursor()

        self.change_screen("splash")
        self.t = 30

    # def build_app(self):

    def build(self):
        """
        The build function is used to build the app. It returns a ScreenManager
        instance that contains all of your screens, which you can add to by using
        the .add_widget() method. The docstring above it explains what the build function does.

        :param self: Access variables that belongs to the class
        :return: The screenmanager
        :doc-author: Trelent
        """

        # self.wm = WindowManager()
        # self.path = Storage().storage()
        # print(self.path)
        # self.screens_store = JsonStore(f"models/screens.json")
        # print(f"screen_store:: {self.screens_store}")
        # self.screen_history = []
        # # self.screen_history = ListProperty()

        # self.amount_store = JsonStore(f"{self.path}/expenses.json")

        # self.current = str(today_date).split("-")
        # self.month_year = f"{self.current[0]}-{self.current[1]}"

        # self.conn = DatabaseManager().conn
        # self.cursor = self.conn.cursor()

        # self.change_screen("login", switch=False)
        # self.change_screen("home")
        # self.t = 30

        # self.wm.get_screen(
        #     "login").ids['email'].text = f"h@g.com"
        # self.wm.get_screen(
        #     "login").ids['password'].text = f"Qwerty1#"

        self.theme_cls.primary_hue = "A100"
        self.theme_style = "Dark"  # "Light"
        self.theme_cls.material_style = "M3"
        # self.theme_cls.theme_style = "Dark"

        return self.wm

    def on_start(self):
        """
        The on_start function is called when the app first starts.
        It schedules a function to run after the splash screen has been shown,
        and then waits for that function to finish before returning.

        :param self: Access the attributes and methods of the class inside a method
        :return: The following:
        :doc-author: Trelent
        """
        Clock.schedule_once(lambda ev: self.post_build_init(ev), 1)

        Clock.schedule_once(self.after_splash, 10)

    def post_build_init(self, ev):
        """
        The post_build_init function is called after the build function of the Kivy app. 
        It binds a keyboard event handler to EventLoop.window, which is an instance of WindowBase, 
        a base class for all window implementations in Kivy. The on_keyboard method of EventLoop will be called when a key press occurs.

        :param self: Access the attributes and methods of the class inside a method
        :param ev: Pass the event object to the function
        :return: The function that is bound to the on_keyboard event of the window
        :doc-author: Trelent
        """

        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        """
        The hook_keyboard function is used to capture the escape key and close the application.
        The function checks if the current screen is login or home, if it is then it will pop a exit popup.
        If not, then it will go back to previous screen.

        :param self: Access the class attributes and methods
        :param window: Get access to the window object
        :param key: Check if the user has pressed any key on the keyboard
        :param *largs: Catch all the extra parameters that are passed to the function
        :return: True if the user presses the escape key
        :doc-author: Trelent
        """

        if key == 27:

            print(self.wm.current)
            if(self.wm.current == 'login'):
                self.exit_popup()
            if(self.wm.current == 'home'):
                self.exit_popup()
            else:
                self.goback()
            return True

    def after_splash(self, *args):
        """
        The after_splash function is called after the splash screen has been shown.
        It changes the screen to login.

        :param self: Access the attributes and methods of the class in python
        :param *args: Pass a variable number of arguments to a function
        :return: The login screen
        :doc-author: Trelent
        """

        self.change_screen("login")

    def fetch_budget(self):
        """
        The fetch_budget function is used to fetch the budget of a particular month.
        It takes in no parameters and returns the budget for that month.

        :param self: Access variables that belongs to the class
        :return: The budget of the user for the month
        :doc-author: Trelent
        """
        try:
            email = self.wm.get_screen("login").ids['email'].text
        except Exception:
            notify.Notify().notify("Unable to get email", error=True)
        sql = "SELECT * FROM budget WHERE email=?"
        # sql = "SELECT * FROM budget WHERE email=? AND strftime('%Y-%m', budget) =?"
        self.cursor.execute(sql, (email,))
        # self.cursor.execute(sql, (email,))
        # global result
        result = self.cursor.fetchall()

        print(f"budget_result: {result}")
        if result:
            for value in result:
                if self.month_year in value[3]:
                    print(self.month_year)
                    budget = value[2]
                    return budget
                    break

            else:
                return print("tada:::: You have not any budget for this month")

    def fetch_expenses(self, limited=True):
        """
        The fetch_expenses function fetches all the amount spent for the month from the database

        :param self: Access variables that belongs to the class
        :return: The total amount spent for the month
        :doc-author: Trelent
        """

        """Fetches all the amount spent for the month from the database"""
        email = self.wm.get_screen("login").ids['email'].text

        if limited == True:
            limit = 6
            sql_limited = "SELECT * FROM expenses WHERE email=? ORDER BY id DESC LIMIT ?"
            self.cursor.execute(sql_limited, (email, limit))
        else:
            sql_unlimited = "SELECT * FROM expenses WHERE email=? AND date LIKE ? ORDER BY id DESC"
            self.cursor.execute(sql_unlimited, (email, f'%{self.month_year}%'))
        # sql_expense = "SELECT price FROM expenses WHERE email=? AND strftime('%Y-%m', price) =?"

        # global result
        result = self.cursor.fetchall()
        self.change_screen("home", switch=False)
        print(f"expense_result: {result}")
        if result:
            price_list = []

            # self.change_screen("home")
            self.wm.get_screen(
                "home").ids['expense_container'].clear_widgets()
            for value in result:
                if self.month_year in value[5]:
                    # break
                    # for price in result[0]:
                    price = value[3]
                    price_no_comma = value[3]
                    item = value[2]
                    date = value[5]
                    icon = value[4].lower()
                    category = value[4].upper()
                    if "," in price_no_comma:
                        price_no_comma = price_no_comma.replace(",", "")
                    price_list.append(int(price_no_comma))

                    self.wm.get_screen(
                        "home").ids['expense_container'].add_widget(ExpenseList(category=category, icon=icons[icon], amount=price, date=date, item=item))
            price = sum(price_list)
            # print(f"price_sum: {price}")
            # self.amount_store.put("total_expenses", total = price)
            return price

    def login(self, email, password):
        """
        The login function is used to login into the app. It takes in an email and a password as parameters, checks if they are valid and then logs in the user.

        :param self: Access the attributes and methods of the class in python
        :param email: Fetch the email from the database
        :param password: Encrypt the password before storing it in the database
        :return: A list of tuples
        :doc-author: Trelent
        """

        sql = "SELECT * FROM user_info WHERE email=? AND password=?"
        self.cursor.execute(sql, (email, password))
        # global result
        result = self.cursor.fetchall()

        print(f"user: {result}")
        if result:
            name = result[0][1]

            if self.fetch_budget() != None:
                self.calculate_expenses_and_percentage(if_login=True)
                self.reset_btn_text_login()
                self.wm.get_screen(
                    "home").ids['greeting'].text = f"Hi, {name.title()} "
            else:
                self.reset_btn_text_login()
                self.change_screen("budget")
                self.change_screen("home", switch=False)
                self.wm.get_screen(
                    "home").ids['percentage'].text = "0 %"

                self.wm.get_screen(
                    "home").ids['greeting'].text = f"Hi, {name.capitalize()}"
                return notify.Notify().notify("You have not any budget for this month", error=True)

        else:
            self.reset_btn_text_login()
            notify.Notify().notify("invalid email or password", error=True)

    def login_loader(self, email, password):


        self.wm.get_screen('login').ids['btn'].text = "Verifying..."

        Clock.schedule_once(lambda x: self.login(email, password), 2)

    def reset_btn_text_login(self):
        """
        The reset_btn_text_login function resets the text of the login screen's proceed button to &quot;Proceed&quot; after it has been changed by pressing the  button.
        
        :param self: Access the attributes and methods of the class
        :return: &quot;proceed&quot;
        :doc-author: Trelent
        """
        
        self.wm.get_screen('login').ids['btn'].text = "Proceed"

    def fetch_total_expenses_from_db(self, *args):
        """
        The fetch_total_expenses_from_db function is used to fetch the total expenses from the database.
        It takes in a string argument of email and returns an integer value of price.
        
        :param self: Access variables that belongs to the class
        :param *args: Pass a variable number of arguments to a function
        :return: The total expenses for the current month
        :doc-author: Trelent
        """
        
        email = self.wm.get_screen("login").ids['email'].text

        sql_unlimited = "SELECT price FROM expenses WHERE email=? AND date LIKE ? ORDER BY id"
        self.cursor.execute(sql_unlimited, (email, f'%{self.month_year}%'))
        # sql_expense = "SELECT price FROM expenses WHERE email=? AND strftime('%Y-%m', price) =?"

        # global result
        result = self.cursor.fetchall()
        if result:
            price_list = []

            # self.change_screen("home")

            for value in result:
                # break
                # for price in result[0]:
                price = value[0]
                if "," in price:
                    price = price.replace(",", "")
                price_list.append(int(price))

            price = sum(price_list)
            # print(f"price_sum: {price}")
            # self.amount_store.put("total_expenses", total = price)
            self.update_expenses(price)
            return price

    def toggle_amount(self):
        """
        The toggle_amount function is used to toggle the amount of money spent.
        It takes in no parameters and returns an integer value.

        :param self: Access the class attributes and methods
        :return: The total amount of money spent on expenses
        :doc-author: Trelent
        """

        if self.amount_store.exists("total_expenses"):
            total = self.amount_store.get("total_expenses")["total"]
            total = (format(int(total),  ',d'))
            print(total)

            return total

    def get_total_expenses(self):
        """
        The get_total_expenses function returns the total amount of expenses in the store.


        :param self: Access the attributes and methods of the class in python
        :return: The total amount of expenses in the store
        :doc-author: Trelent
        """

        if self.amount_store.exists("total_expenses"):
            total = self.amount_store.get("total_expenses")["total"]
            return total

    def update_expenses(self, total_expenses):
        """
        The update_expenses function updates the total expenses in the amount_store.


        :param self: Access the attributes and methods of the class in python
        :param total_expenses: Store the total amount of expenses for a given month
        :return: The total_expenses variable
        :doc-author: Trelent
        """

        self.amount_store.put("total_expenses", total=total_expenses)

    def calculate_expenses_and_percentage(self, if_login: bool):
        """
        The calculate_expenses_and_percentage function is used to calculate the total expenses and percentage of budget spent.
        It takes in a name as an argument, fetches the budget from the database and calculates both total expenses and percentage of budget spent.
        The function then displays these values on screen.

        :param self: Access the class attributes and methods
        :param name: Fetch the name of the user from the database
        :return: The total expenses, the percentage and the budget
        :doc-author: Trelent
        """

        budget = self.fetch_budget()
        if "," in str(budget):
            budget = budget.replace(",", "")
        budget = int(budget)
        if if_login == True:
            # total_expenses = self.get_total_expenses()
            total_expenses = self.fetch_total_expenses_from_db()
            self.fetch_expenses()
        else:
            total_expenses = self.get_total_expenses()
            # Clock.schedule_once(
            # lambda x: self.update_expenses(total_expenses), 2)
        if total_expenses == None:
            total_expenses = 1
            notify.Notify().notify("You have made no expenses yet", error=True)
            percentage = (total_expenses/budget) * 100
        else:
            percentage = (total_expenses/budget) * 100
        print(
            f"tottal: {total_expenses} %: {percentage}%, budget: {budget}")

        self.wm.get_screen(
            "home").ids['limit_bar'].set_value = percentage

        self.wm.get_screen(
            "home").ids['amount'].text = "XXXX.XX NGN"

        self.wm.get_screen(
            "home").ids['month_year'].text = f"{date_dict[self.current[1][1]]}, {self.current[0]}"  # fetches the date and displays it on the homescreen

        if percentage <= 25:

            self.wm.get_screen(
                "home").ids['limit_bar'].bar_color = self.colors.get('success')
            self.wm.get_screen(
                "home").ids['percentage'].text_color = self.colors.get('success')
        if percentage > 25 and percentage <= 50:

            self.wm.get_screen(
                "home").ids['limit_bar'].bar_color = self.colors.get('yellow')
            self.wm.get_screen(
                "home").ids['percentage'].text_color = self.colors.get('yellow')
        if percentage > 50 and percentage <= 75:

            self.wm.get_screen(
                "home").ids['limit_bar'].bar_color = self.colors.get('orange')
            self.wm.get_screen(
                "home").ids['percentage'].text_color = self.colors.get('orange')
        if percentage > 75 and percentage <= 100:

            self.wm.get_screen(
                "home").ids['limit_bar'].bar_color = self.colors.get('warning')
            self.wm.get_screen(
                "home").ids['percentage'].text_color = self.colors.get('warning')

            notify.Notify().notify(
                f"You have exhausted [color=#b90000]{str(round(percentage))}% of your budget[/color]\n You should reduce your expenses", method="dialog")

        if percentage > 100:

            self.wm.get_screen(
                "home").ids['limit_bar'].bar_color = self.colors.get('warning')
            self.wm.get_screen(
                "home").ids['percentage'].text_color = self.colors.get('warning')

            notify.Notify().notify(
                f"You have exhausted {str(round(percentage))}% of your budget\n You have spent more than your allocated budget could account for.", method="dialog")

        self.wm.get_screen(
            "home").ids['percentage'].text = f"{str(round(percentage))}%"

        self.change_screen("home")
        Clock.schedule_once(self.fetch_total_expenses_from_db, 2)

    def go_to_otp(self, email):
        """
        The go_to_otp function is used to generate a random OTP and send it to the user's email.
        It also starts a countdown timer that will automatically expire the OTP  if it isn't used on time.

        :param self: Access the class variables
        :param email: Send the otp to the user's email address
        :return: The otp generated by the generate_otp function
        :doc-author: Trelent
        """

        sql = "SELECT * FROM user_info WHERE email = ?"
        self.cursor.execute(sql, (email,))
        result = self.cursor.fetchall()
        if result:
            self.change_screen("otp", switch=False)
            self.wm.get_screen("otp").ids['first'].focus = True
            # print("{self.generate_otp()}")
            otp = str(self.generate_otp())
            self.wm.get_screen("otp").ids['otp_lbl'].text = otp
            self.change_screen("otp")
            if self.wm.has_screen("otp"):

                Clock.schedule_once(lambda x: self.emailer(email, otp), 1)
                self.change_screen("otp")
                Clock.schedule_interval(self.countdown, 1)
        else:
            notify.Notify().notify("Email not found", error=True)

    def emailer(self, recipient, otp):
        """
        The emailer function sends an email to the recipient with the OTP.


        :param self: Access the class variables
        :param recipient: Specify the email address of the recipient
        :param otp: Store the one time password that is generated by the send_email function
        :return: A print statement
        :doc-author: Trelent
        """

        send_email(recipient=recipient, otp=otp)
        print("Email sent")

    def resend_otp(self):
        """
        The resend_otp function is used to resend the otp to the user's email address.
        It takes in no parameters and returns nothing.

        :param self: Access variables that belongs to the class
        :return: The otp that is generated and sent to the user
        :doc-author: Trelent
        """

        email = self.wm.get_screen("forgot").ids['email'].text
        otp = str(self.generate_otp())
        self.wm.get_screen("otp").ids['otp_lbl'].text = otp
        self.change_screen("otp")
        if self.wm.has_screen("otp"):

            Clock.schedule_once(lambda x: self.emailer(email, otp), 1)
            self.change_screen("otp")
            Clock.schedule_interval(self.countdown, 1)

    def generate_otp(self):
        """
        The generate_otp function generates an OTP and stores it in a variable.
        It then returns the value of the otp to be used later.

        :param self: Access variables that belongs to the class
        :return: A 4 digit random number
        :doc-author: Trelent
        """

        # Declare a digits variable
        # which stores all digits
        digits = "0123456789"
        OTP = ""

        # length of password can be changed
        # by changing value in range
        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]

        print(f"otp:::: {OTP}")

        return OTP

        # define the countdown func.

    def countdown(self, *args):
        """
        The countdown function is used to count down the time left for the user to enter their OTP.
        It starts at 30 seconds and counts down by 1 second until it reaches 0, then stops.

        :param self: Access variables that belongs to the class
        :param *args: Pass a variable number of arguments to a function
        :return: The value of self
        :doc-author: Trelent
        """

        # time.sleep(1)

        self.wm.get_screen("otp").ids['timer'].text = f"{str(self.t)} secs"
        self.t -= 1

        if self.t == 0:
            Clock.unschedule(self.countdown)
            otp = str(
                self.generate_otp())
            self.wm.get_screen("otp").ids['timer'].text = "0 secs"
            self.wm.get_screen("otp").ids['otp_lbl'].text = otp

            self.t = 30
            notify.Notify().notify("OTP Expired")

    def expense_loader(self,  item, price, category):

        self.wm.get_screen('add_expense').ids['btn'].text = "Verifying..."

        Clock.schedule_once(
            lambda x: self.save_expense(item, price, category), 2)

    def reset_btn_text_expense(self):
        self.wm.get_screen('add_expense').ids['btn'].text = "Save"

    def save_expense(self, item, price, category):
        """
        The save_expense function saves the expense to the database.
        It takes in 3 parameters, item, price and category.
        The function checks if all fields are filled out before saving it to the database. 
        If they are not filled out then an error message is displayed on screen.

        :param self: Access the attributes and methods of the class in python
        :param item: Store the item that is bought
        :param price: Store the price of the item bought
        :param category: Determine which category the expense belongs to
        :return: None
        :doc-author: Trelent
        """
        # try:
        email = self.wm.get_screen("login").ids['email'].text
        # except Exception:
        #     notify.Notify().notify("Unable to get email", error=True)

        if email == "" or item == "" or category == "" or price == "":
            notify.Notify().notify("All fields must be filled", error=True)
            self.reset_btn_text_expense()
        else:
            sql = "INSERT INTO expenses (email, item_bought, price, category_name, date) VALUES (?,?,?,?,?)"
            self.cursor.execute(
                sql, (email, item, price, category, today_date))
            self.conn.commit()
            self.reset_btn_text_expense()
            notify.Notify().notify("expense updated successfully")
            self.wm.get_screen("home").ids['expense_container'].clear_widgets()
            self.fetch_expenses()
            # self.wm.get_screen(
            #     "home").ids['expense_container'].add_widget(ExpenseList(category=category.upper(), icon=icons[category.lower()], amount=price, date=str(today_date), item=item))

            self.calculate_expenses_and_percentage(if_login=False)

            # if self.amount_store.exists("total_expenses"):
            total = self.amount_store.get("total_expenses")['total']
            print(f"total1 :: {total}")
            total2 = total + int(price.replace(",", ""))
            print(f"total2 :: {total2}")
            Clock.schedule_once(
                lambda x: self.update_expense_after_save(total2))

    def update_expense_after_save(self, total):
        print(self.amount_store.put("total_expenses", total=total))

        # self.manager.get_screen(
        # "home").ids['expense_container'].text =
        self.change_screen("home")

    def update_dialog(self):
        """
        The update_dialog function creates a popup that allows the user to update their budget.
        It takes no parameters and returns nothing.
        
        :param self: Access the instance of the class
        :return: The instance of the update_popup
        :doc-author: Trelent
        """
        
        self.update_popup = Pop(title="Update Budget",
                                type="custom",
                                content_cls=UpdateBudgetContent(),)
        self.update_popup.open()

    def update_budget(self, budget):
        """
        The update_budget function updates the budget for a given month.
        It takes in a string representing the new budget and adds it to the old budget.
        The function then commits this change to the database.

        :param self: Access the class attributes and methods
        :param budget: Update the budget in the database
        :return: The updated budget
        :doc-author: Trelent
        """

        email = self.wm.get_screen("login").ids['email'].text
        old_budget = self.fetch_budget()
        # old_budget = old_budget.replace(
        #     ",", "") if "," in old_budget1 else old_budget1
        print(f"budget: {budget}")
        print(f"old_budget: {old_budget}")
        new_budget = int(budget) + int(old_budget)
        sql = "UPDATE budget SET budget= ? WHERE email = ? AND date LIKE ? "
        run = self.cursor.execute(
            sql, (new_budget, email, f'%{self.month_year}%'))
        if run:
            print(f"run {run}")
            self.conn.commit()
            self.update_popup.dismiss(force=True)
            notify.Notify().notify("Budget Updated")

    def show_all_expenses(self, *args):
        """
        The show_all_expenses function is used to display all expenses in the database.
        It takes no arguments and returns nothing.
        
        :param self: Access the instance of a class
        :param *args: Pass a variable number of arguments to a function
        :return: All of the expenses in the database
        :doc-author: Trelent
        """
        
        # self.limit = 0
        self.fetch_expenses(limited=False)
        self.wm.get_screen("home").ids['spinner'].active = False

    def show_all_expenses_loader(self):
        """
        The show_all_expenses_loader function is used to load all expenses from the database and display them on the screen.
        It does this by clearing any widgets that are currently on the expense_container, then scheduling a function call to show_all_expenses after 2 seconds.
        
        
        :param self: Access the class attributes and methods
        :return: The expense_container widget of the home screen
        :doc-author: Trelent
        """
        
        self.wm.get_screen("home").ids['spinner'].active = True
        self.wm.get_screen("home").ids['expense_container'].clear_widgets()

        Clock.schedule_once(self.show_all_expenses, 2)

    def change_screen(self, screen_name, switch=True, __from_goback=False):
        """
        The change_screen function changes the screen to a specified screen.
        It checks if the screen already exists in the ScreenManager, and if it does not exist,
        it creates a new instance of that class and adds it to the ScreenManager. It then changes
        the current screen to that specified.

        :param self: Access the attributes and methods of the class in python
        :param screen_name: Specify the screen that will be shown
        :param switch: Switch between screens
        :param __from_goback: Prevent the screen history from being updated when the user is going back to a previous screen
        :return: The screen manager object
        :doc-author: Trelent
        """

        # self.wm.current = screen_name
        # checks if the screen already exists in the screen manager
        # if the screen is not yet in the screen manager,
        if not self.wm.has_screen(screen_name):
            # gets the key screen name from the screens.json file
            getter = self.screens_store.get(screen_name)
            # executes the value of the import key in the screens.json file
            exec(getter['import'])

            print(getter['object'])
            print(getter['import'])
            print(getter['kv'])

            # calls the screen class to get the instance of it
            screen_object = eval(getter["object"])
            # automatically sets the screen name using the arg that passed in set_current
            screen_object.name = screen_name
            # Builder.load_file(getter['kv'])
            # finnaly adds the screen to the screen-manager
            self.wm.add_widget(screen_object)
            # changes the screen to the specified screen
            # self.wm.current = screen_name
            # Builder.load_file(getter['kv'])

        # if the screens is already in the screen manager,
        # changes the screen to the specified screen
        if switch == True:
            self.wm.current = screen_name

        # if not __from_goback:
        if screen_name != "loader":
            self.screen_history.append({"name": screen_name, })

    def goback(self):
        """
        The goback function allows the user to go back one screen in the application.


        :param self: Access the class attributes
        :return: The previous screen
        :doc-author: Trelent
        """

        if len(self.screen_history) > 1:
            self.screen_history.pop()
            prev_screen = self.screen_history[-1]
            print(self.screen_history)
            print(prev_screen)

            self.change_screen(prev_screen["name"])

    def logout(self):
        """
        The logout function is used to logout of the application. It will change the screen back to login

        :param self: Access the class attributes
        :return: The screen name &quot;login&quot;
        :doc-author: Trelent
        """

        self.change_screen("login")

    def exit_popup(self):
        """
        The exit_popup function creates a popup window that asks the user if they want to exit the app.
        If yes, then it closes the app. If no, then it does nothing.

        :param self: Access the class attributes and methods
        :return: A pop object
        :doc-author: Trelent
        """

        exit_btn = RoundButton(text="Exit", md_bg_color=self.colors.get(
            "orange"), on_press=lambda *args: self.exit())
        cancel_btn = FlatButton(
            text="Go back", on_press=lambda *args: self.do_not_exit())
        self.exit_popup = Pop(title="Close app", text="Are you sure you want to exit app?", buttons=[
                              cancel_btn, exit_btn])

        self.exit_popup.open()

    def do_not_exit(self, *args):
        """
        The do_not_exit function is used to prevent the user from exiting out of a popup that has been
        opened by pressing the X button on the top right corner. This function is called when you press
        the &quot;Do not exit&quot; button in any popup.

        :param self: Access the attributes and methods of the class in python
        :param *args: Pass a variable number of arguments to a function
        :return: Nothing
        :doc-author: Trelent
        """

        self.exit_popup.dismiss()

    def exit(self, *args):
        """
        The exit function stops the program from running.

        :param self: Refer to the object that is calling the function
        :param *args: Pass a variable number of arguments to the function
        :return: The value none
        :doc-author: Trelent
        """

        self.stop()
