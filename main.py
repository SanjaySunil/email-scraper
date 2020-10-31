"""
 * Email Scraper
 * Author: Sanjay Sunil (a.k.a D3VSJ)
 * License: MIT
"""

# Imports

import uuid
import time
import os
import webbrowser

# Variables
ans = True    
strURL = "https://github.com/D3VSJ/Email-Scraper"

# Functions
# Clear Console
def clear():
    return os.system('cls')
# Email Scraper
def emailScraper():
    count = 0
    print("---------------------------STARTING IN---------------------------")
    print("                               3                                 ")
    time.sleep(0.9)
    print("                               2                                 ")
    time.sleep(0.9)
    print("                               1                                 ")
    print("-----------------------------------------------------------------")
    time.sleep(0.9)
    clear()
    exists = os.path.isfile('emails.txt')
    if exists:
        file = open("emails.txt", "a")
    else:
        file = open("emails.txt", "w+")
    while 2 > 1:
        rand = str(uuid.uuid4())
        link = 'fyii.de/trashmail/'
        email_address = '@fyii.de'
        email_link = link+rand[:8]+'.html'
        email = rand[:8]+email_address
        print("---------------------------Email Scraper---------------------------")
        print("                        Emails Scraped:", count                     )
        print("                         "+ email                                   )
        print("                   "+ email_link                                    )
        print("-------------------------------------------------------------------")
        clear()
        file.write(email+'\n'+email_link+'\n')
        file.write('\n')
        count += 1
# Opens GitHub link in default browser
def githubLink():
    webbrowser.open(strURL, new=2)

# Menu 
while ans:
    clear()
    print("""
---------------------------Email Scraper---------------------------
                           Sanjay Sunil
1. Scrape Emails
2. GitHub
3. Exit/Quit

-------------------------------------------------------------------
    """)
    ans = input("Enter your choice: [0-3] ")
    if ans == "1":
        clear()
        emailScraper()
    elif ans == "2":
        githubLink()
        ans = True
        clear()
    elif ans == "3":
        clear()
        print("\nGoodbye! Thank you for using Email Scraper!")
        exit()
    elif ans != "":
        clear()
        print("\nNot a valid choice! Please try again!")
        time.sleep(1)

