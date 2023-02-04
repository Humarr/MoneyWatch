import sqlite3
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import re
from models.database import DatabaseManager
from kivy.clock import Clock
from widgets import notify


class IntegrityErrorSql(BaseException):
    try:
        DatabaseManager().integrity_error
    except Exception as e:
        print(f"integrity_error_sql: {e}")


class SignupScreen(MDScreen):
    Builder.load_file("views/signup.kv")

    conn = DatabaseManager().conn
    cursor = conn.cursor()

    def validate_password(self, password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

        # compiling regex
        pat = re.compile(reg)

        # searching regex
        valid = re.search(pat, password)

        if valid:
            return True
        else:
            return False

        # return val

    def validate_email(self, email):
        pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu)"
        validated = re.search(pattern, email)
        return validated

    def signup(self, name, email, password):
        """
        The signup function is used to create a new user account. It takes in the name, email and password of the user as parameters.
        It then checks if the email address is valid and if it's not, it displays an error message on screen. If it's valid, 
        it checks if there are any other accounts registered with that same email address already present in our database by querying our database for all emails currently stored within our system. If no such emails are found, we proceed to insert this new account into our database along with its corresponding username and password.

        :param self: Access variables that belong to the class
        :param name: Set the username
        :param email: Validate the email address
        :param password: Validate the password entered by the user
        :return: The email and password validated
        :doc-author: Trelent
        """
        # email = ""
        DatabaseManager().build_tables()
        if not self.validate_email(email):
            email_validated = email
            print(email_validated)
            notify.Notify().notify("Please enter a valid email address", error=True)
            self.reset_btn_text_signup()
        elif not self.validate_password(password):
            password_validated = password
            print(password_validated)
            notify.Notify().notify(
                "Password must: be at least 6 characters, have a digit, letter, uppercase letter and a symbol", "dialog")
            self.reset_btn_text_signup()
        else:
            try:
                # sql = "SELECT * FROM user_info"
                # sql_run = self.cursor.execute(sql)
                # res = sql_run.fetchall()
                # if res == []:
                sql = "INSERT INTO user_info (username, email,  password) VALUES (?, ?, ?)"
                self.cursor.execute(sql, (name, email, password))
                notify.Notify().notify("Account created successfully")
                self.manager.current = "login"
                self.conn.commit()
                self.reset_btn_text_signup()
                # else:
                #     Notify().notify("Can't register more than one account", error=True)
            # except DatabaseManager().integrity_error:
            except sqlite3.IntegrityError:
                self.reset_btn_text_signup()

                notify.Notify().notify("Email already registered", error=True)

    def signup_loader(self, name, email, password):
        """
        The signup_loader function is called when the user clicks on the signup button. 
        It takes in 3 parameters: name, email and password. It then calls the signup function with these parameters.

        :param self: Access the attributes and methods of the class in python
        :param name: Store the name of the user
        :param email: Store the email address entered by the user
        :param password: Store the password entered by the user
        :return: The value of the signup function
        :doc-author: Trelent
        """

        self.ids['btn'].text = "Verifying..."

        Clock.schedule_once(lambda x: self.signup(name, email, password), 2)

    def reset_btn_text_signup(self):
        """
        The reset_btn_text_signup function resets the text of the button to &quot;Proceed&quot; after a user has signed up.


        :param self: Access the attributes and methods of the class in python
        :return: The text of the button
        :doc-author: Trelent
        """

        self.ids['btn'].text = "Proceed"
