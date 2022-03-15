import webbrowser
from random import randrange

# Web Site List
webSiteList = ["https://github.com/mhmadrashd", "https://www.linkedin.com/in/mhmadrashd/",
               "https://www.google.com/", "https://www.facebook.com/"]

# Open random website from list
webbrowser.open(webSiteList[randrange(4)], new=2)


