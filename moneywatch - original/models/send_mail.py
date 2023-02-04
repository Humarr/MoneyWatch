# import smtplib
# import ssl
# import threading
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
import yagmail
from widgets.notify import Notify


def send_email(recipient, otp):
    try:
        sender_email = "Pynewhorizon@gmail.com"
        receiver_email = recipient
        password1 = "PyNeWhOrIzOn1"
        sender_password = "mkndzcslpskrqacd"
        yag = yagmail.SMTP(sender_email, sender_password)

        subject = "OTP Verification..."
        body = f"Your  One time password for the Money Watch App is {otp}"
        yag.send(receiver_email, subject, body)
    #     s = smtplib.SMTP('smtp.gmail.com', 587)
    #     s.starttls()
    #     sender_email = "Pynewhorizon@gmail.com"
    #     receiver_email = recipient
    #     password1 = "PyNeWhOrIzOn1"
    #     sender_password = "mkndzcslpskrqacd"
    #     message = MIMEMultipart("alternative")
    #     message["Subject"] = "OTP Verification..."
    #     message["From"] = sender_email
    #     message["To"] = receiver_email

    #     # Get the words before the '@' sign in the user's email address
    #     # email = email.split("@")

    # # password = user_name + '123'
    #     # Create the plain-text and HTML version of your message
    #     text = f"""\
    #     Your  One time password for the Money Watch App is {otp}"""

    #     # Turn these into plain/html MIMEText objects
    #     part1 = MIMEText(text, "plain")
    #     # part2 = MIMEText(html, "html")

    #     # Add HTML/plain-text parts to MIMEMultipart message
    #     # The email client will try to render the last part first
    #     message.attach(part1)
    #     # message.attach(part2)

    #     # Create secure connection with server and send email
    #     context = ssl.create_default_context()
    #     server = smtplib.SMTP_SSL(
    #         "smtp.gmail.com", 465, context=context)
    #     server.login(sender_email, sender_password)
    #     server.sendmail(
    #         sender_email, receiver_email, message.as_string()
    #     )

    except Exception as e:
        print(f"Send Email Error{e}")
        Notify().notify(f"No internet connection", error=True)
        # raise e
    # else:
    #     pass


# # Import the following module
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os

# # def send():
# # initialize connection to our
# # email server, we will use gmail here
# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()

# # Login with your email and password
# smtp.login('Pynewhorizon@gmail.com', 'PyNeWhOrIzOn1')


# # send our email message 'msg' to our boss
# def message(subject="OTP verification",
#             text="", img=None,
#             attachment=None):

#     # build message contents
#     msg = MIMEMultipart()

#     # Add Subject
#     msg['Subject'] = subject

#     # Add text contents
#     msg.attach(MIMEText(text))

#     # Check if we have anything
#     # given in the img parameter
#     if img is not None:

#         # Check whether we have the lists of images or not!
#         if type(img) is not list:

#             # if it isn't a list, make it one
#             img = [img]

#         # Now iterate through our list
#         for one_img in img:

#             # read the image binary data
#             img_data = open(one_img, 'rb').read()
#             # Attach the image data to MIMEMultipart
#             # using MIMEImage, we add the given filename use os.basename
#             msg.attach(MIMEImage(img_data,
#                                 name=os.path.basename(one_img)))

#     # We do the same for
#     # attachments as we did for images
#     if attachment is not None:

#         # Check whether we have the
#         # lists of attachments or not!
#         if type(attachment) is not list:

#             # if it isn't a list, make it one
#             attachment = [attachment]

#         for one_attachment in attachment:

#             with open(one_attachment, 'rb') as f:

#                 # Read in the attachment
#                 # using MIMEApplication
#                 file = MIMEApplication(
#                     f.read(),
#                     name=os.path.basename(one_attachment)
#                 )
#             file['Content-Disposition'] = f'attachment;\
#             filename="{os.path.basename(one_attachment)}"'

#             # At last, Add the attachment to our message object
#             msg.attach(file)
#     return msg


# # Call the message function
# msg = message("Good!", "Hi there!",
#             r"C:\Users\Dell\Downloads\Garbage\Cartoon.jpg",
#             r"C:\Users\Dell\Desktop\slack.py")

# # Make a list of emails, where you wanna send mail
# to = ["ABC@gmail.com",
#     "XYZ@gmail.com", "insaaf@gmail.com"]

# # Provide some data to the sendmail function!
# smtp.sendmail(from_addr="hello@gmail.com",
#             to_addrs=to, msg=msg.as_string())

# # Finally, don't forget to close the connection
# smtp.quit()
