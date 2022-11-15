"""
 * Email Scraper Class
 * Author: Sanjay Sunil
 * License: MIT
"""

import uuid
import os
import webbrowser


class EmailScraper:
    def __init__(self, file_path):
        self._DOMAIN = "fyii.de/trashmail/"
        self._EMAIL_DOMAIN = "@fyii.de"
        self._GITHUB_URL = "https://github.com/sanjaysunil/email-scraper"
        self._file_path = file_path

    def __clear_screen(self):
        os.system('clear')

    def __scrape(self):
        random_uuid = str(uuid.uuid4())
        email_link = self._DOMAIN+random_uuid[:8]+'.html'
        email = random_uuid[:8]+self._EMAIL_DOMAIN
        return email, email_link

    def __start(self, emails):
        scraped_emails = 0
        exists = os.path.isfile(self._file_path)

        if exists:
            file_handler = open(self._file_path, "a")
        else:
            file_handler = open(self._file_path, "w+")

        while scraped_emails != emails:
            email, email_link = self.__scrape()
            file_handler.write(email+'\n'+email_link+'\n'+'\n')
            scraped_emails += 1

        file_handler.close()

    def menu(self):
        OPTIONS = [["Scrape 1 Email"], ["Scrape Multiple Emails"], [
            "GitHub"], ["Exit"]]
        self.__clear_screen()

        while True:
            self.__clear_screen()
            print("Email Scraper\n")
            for count, option in enumerate(OPTIONS):
                print(f"{count+1}: {option[0]}")
            option = int(input("Choose an option: "))

            if option == 1:
                self.__start(1)
                back_to_menu = input(
                    f'Added 1 email to {self._file_path}!\n\nPress enter to go back to menu. ')
            elif option == 2:
                emails = int(input("Emails to scrape: "))
                self.__start(emails)
                back_to_menu = input(
                    f'Added {emails} emails to {self._file_path}!\n\nPress enter to go back to menu. ')

            elif option == 3:
                webbrowser.open(self._GITHUB_URL)

            else:
                try_again = input(
                    'Invalid option, please enter to try again. ')
