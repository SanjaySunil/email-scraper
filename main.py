"""
 * Email Scraper
 * Author: Sanjay Sunil
 * License: MIT
"""

from src.email_scraper import EmailScraper

scraper = EmailScraper(file_path='emails.txt')
scraper.menu()
