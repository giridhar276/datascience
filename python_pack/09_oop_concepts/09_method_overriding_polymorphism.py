class Notification:
    def send(self):
        return "Sending generic notification"

class EmailNotification(Notification):
    def send(self):
        return "Sending email"

class SMSNotification(Notification):
    def send(self):
        return "Sending SMS"

for notification in [EmailNotification(), SMSNotification()]:
    print(notification.send())
