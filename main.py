import time

from notification import get_unread_messages_and_notifications
from save import save_data_to_csv
from easygui import passwordbox
from mail import send_email
import schedule
# Prompt the user to enter the password
def inputs():
    print("Enter User credentials")
    username = input("Enter your username: ")
    password = passwordbox('Password:')
    sender_email = input("Enter sender's email address: ")
    receiver_email = input("Enter receiver's email address: ")
    return username, password, sender_email, receiver_email
def func(username, password, sender_email, receiver_email):
    a, b = get_unread_messages_and_notifications(username, password)
    output_file = 'record.csv'
    save_data_to_csv(username, output_file, a, b)

    subject = 'unread messages and notifications'
    message = 'unread messages: ' + a + '\n' + 'unread notifications: ' + b
    send_email(sender_email, receiver_email, subject, message)
if __name__ == '__main__':
    username, password, sender_email, receiver_email = inputs()
    schedule.every(3).hours.do(func, username, password, sender_email, receiver_email)
    while True:
        schedule.run_pending()
        time.sleep(1)
