import selenium
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def get_unread_messages_and_notifications(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    email_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    email_input.send_keys(username)
    password_input.send_keys(password)
    # Submit the login form
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    # Wait until the page has loaded and the user avatar appears (indicating a successful login)
    time.sleep(10)
    # Go to the notifications page
    # driver.get('https://www.linkedin.com/notifications/')
    time.sleep(4)
    notifications = driver.find_elements(By.CSS_SELECTOR, 'span.notification-badge__count')
    notification_texts = [notification.text for notification in notifications]
    if(len(notification_texts)>0):
        print(notification_texts[0])
    time.sleep(4)
    # Get the unread messages
    unread_messages = driver.find_elements(By.CSS_SELECTOR, 'span.notification-badge__count')
    unread_messages_texts = [unread_message.text for unread_message in unread_messages]
    print(unread_messages_texts[0])

    return unread_messages_texts[0], notification_texts[0]
