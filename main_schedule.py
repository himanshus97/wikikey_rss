"""
Main_schedule.py

it's used to run whole code using BeautifulSoup every day 12:00am 

"""

from bin import rsstitle
import schedule

def main():
    print("\t\t---EXTRACTION STARTED---")
    rsstitle.soup()
    print("\t\t---EXTRACTION DONE---")

schedule.every().day.at("00:00").do(main) 


while True:
    schedule.run_pending() 
