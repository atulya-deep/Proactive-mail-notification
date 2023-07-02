# Proactive Mail-Notification
Proactive Mail Notification is a system that is designed to periodically check the user's LinkedIn profile for unread messages and notifications. </br>
The system will store the retrieved data in a CSV file and also send an email notifications to the user's Gmail account. </br>
These notifications will include information about the number of unread messages and other notifications, along with a comparison with the previous occurrence.</br></br>
In today's fast-paced world, keeping track of LinkedIn messages and notifications can be challenging. This system aims to provide users with a proactive approach to stay updated on their LinkedIn activity by receiving regular email updates.

## Installation
Clone this repository to your local machine.

```bash
gh repo clone atulya-deep/Proactive-mail-notification
```
## OUR SOLUTIONS
**`Function Separation:`** Each function is separated into different Python files, ensuring modularity and maintainability. This allows for easier management and future enhancements to specific functionalities.

**`Selenium for GUI Interaction:`** The Selenium Python library is utilized for interacting with the LinkedIn GUI. It enables automated login and retrieval of unread messages and notifications from the user's LinkedIn profile.

**`Data Storage in CSV:`** The fetched data, including unread messages and notifications, is stored in a CSV file. The data is accompanied by a timestamp, providing a historical record of the user's LinkedIn activity.

**`Scheduler and SMTP for Periodic Notifications:`** To enable periodic notifications to the user, a scheduler is implemented. The scheduler triggers the notification process at regular intervals. The SMTP library is used for email delivery, ensuring that the user receives the notification in their Gmail account.

**`Password Protection:`** To safeguard passwords, the easy gui library is used for secure password input. The cryptography library provides encryption and decryption functionalities, ensuring password security during storage and transmission.

## Architecture Diagramming
![image](https://github.com/atulya-deep/Proactive-mail-notification/assets/90817926/f05f06c3-915e-46bf-a618-c9bd4cda5f61)
