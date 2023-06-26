import csv
import datetime
def save_data_to_csv(username,output_file,unread_messages, notifications):
    """Saves the data to a CSV file."""
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['username','Unread Messages', 'unread Notifications', 'Timestamp'])
        writer.writerow([username,unread_messages, notifications, datetime.datetime.now()])