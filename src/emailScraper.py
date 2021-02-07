# Imports

import uuid
import time
import os

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