from instabot import Bot
import time, sched

# Remember to delete config file before launch

Username = input("Enter your Instagram username: ")
Password = input("Enter your Instagram password: ")
Targetuser = input("Enter the recipient's username: ")
TargetMessage = input("Enter the message you would like to send: ")
Logintime = input("Scheduled login time (Fri Sep 09 HH:MM:SS YYYY): ")
Sendtime = input("Scheduled send time (Fri Sep 09 HH:MM:SS YYYY): ")

print()
bot = Bot()


def Login():
    bot.login(username=Username, password=Password)
    print("Log in complete")


def SendMessage():
    bot.send_message(TargetMessage, Targetuser)
    print("Message sent!")


s = sched.scheduler(time.time, time.sleep)
s.enterabs(time.mktime(time.strptime(Logintime)), 0, Login)
s.enterabs(time.mktime(time.strptime(Sendtime)), 0, SendMessage)

print(f"\nLaunched with parameters:\nUsername: {Username}\nPassword:{Password}\nTarget Username: {Targetuser}\nMessage: {TargetMessage}\n")
print("Waiting until the time is right...")
s.run()