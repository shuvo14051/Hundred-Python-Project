"""
By using a third-party application or API to manage the 
functionality of an application, you are automating the application.

```pip install instabot```
"""

from instabot import Bot
bot = Bot()

bot.login(username="username", password="pass")
bot.send_message("You are too cute!", ["receiver user name"])
