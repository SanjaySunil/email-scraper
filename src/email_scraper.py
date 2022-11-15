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
        self._file_path = file_path

    def __scrape(self):
        random_uuid = str(uuid.uuid4())
        email_link = self._DOMAIN+random_uuid[:8]+'.html'
        email = random_uuid[:8]+self._EMAIL_DOMAIN
        return email, email_link

    def start(self, emails):
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
