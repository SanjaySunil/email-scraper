"""
 * Email Scraper
 * Author: Sanjay Sunil
 * License: MIT
"""
import os
import webbrowser
from src.email_scraper import EmailScraper

OPTIONS = ["Scrape 1 Email", "Scrape Multiple Emails",
           "View Project Information", "Exit"]
PROJECT_URL = "https://github.com/sanjaysunil/email-scraper"
os.system('clear')

while True:
    os.system('clear')
    print("Email Scraper\n")
    [print(i+1, OPTIONS[i]) for i in range(len(OPTIONS))]
    print('\n')

    while True:
      try:
        option = int(input("Choose an option: "))
        break
      except ValueError:
        print('Please type an option number.\n')

    if option == 1:
        file_to_write = input('Enter filename to write to: ')
        scraper = EmailScraper(file_path=file_to_write)
        print(scraper.start(1))
        back_to_menu = input(
            f'\n\nPress enter to go back to menu. ')

    elif option == 2:
        while True:
          try:
            emails = int(input("Emails to scrape: "))
            break
          except ValueError:
            print('Please enter a valid number of emails.')

        file_to_write = input('Enter filename to write to: ')
        scraper = EmailScraper(file_path=file_to_write)
        print(scraper.start(emails))
        back_to_menu = input(
            f'\n\nPress enter to go back to menu. ')

    elif option == 3:
        webbrowser.open(PROJECT_URL)

    elif option == 4:
      exit("Thank you for using email-scraper.")

    else:
        try_again = input(
            'Invalid option, please enter to try again. ')
