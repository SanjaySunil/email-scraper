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
        self.__DOMAIN = "fyii.de/trashmail/"
        self.__EMAIL__DOMAIN = "@fyii.de"
        self.__file_path = file_path

    def __scrape(self):
        random_uuid = str(uuid.uuid4())
        email_link = self.__DOMAIN+random_uuid[:8]+'.html'
        email = random_uuid[:8]+self.__EMAIL__DOMAIN
        return email, email_link

    def start(self, emails):
        scraped_emails = 0
        exists = os.path.isfile(self.__file_path)

        try:
          if exists:
              file_handler = open(self.__file_path, "a")
          else:
              file_handler = open(self.__file_path, "w+")

        except FileNotFoundError:
          if self.__file_path == '': return 'Cannot write to a file with no name!'
          else: return 'Cannot write to specified file!'

        while scraped_emails != emails:
            email, email_link = self.__scrape()
            file_handler.write(email+'\n'+email_link+'\n'+'\n')
            scraped_emails += 1

        file_handler.close()

        return f'Added {emails} emails to {self.__file_path}!'
