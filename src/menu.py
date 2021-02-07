import src.emailScraper as app
import os
import webbrowser

strURL = "https://github.com/sanjaysunil/Email-Scraper"

# Clear Console
def clear():
    return os.system('cls')

# Opens GitHub link in default browser
def githubLink():
    webbrowser.open(strURL, new=2)

def menu():
  ans = True    

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
          app.emailScraper()
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