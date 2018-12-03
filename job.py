from easygui import*
import sys
from selenium import webdriver


msg="select your preference"
title="available choices"
choices=["Part time job","Annual job"]
choice=choicebox(msg,title,choices)
	
if choice=="Part time job":
	msg="choose the site"
	choices=["naukri.com","the balance careers.com","indeed.co.in"]
	choice=choicebox(msg,title,choices)
			
	if choice=="naukri.com":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://my.naukri.com/account/createaccount?othersrcp=23531&wExp=N&gclid=Cj0KCQiAxZPgBRCmARIsAOrTHSYsVrsw9LYL6Z8_s0rW6k77buejU1kyA4QhUYJ30Ur12k4xSymV5k0aAu-PEALw_wcB")
	elif choice=="the balance careers.com":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://www.thebalancecareers.com/")
	elif choice=="indeed.co.in":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://www.indeed.jobs/")
elif choice=="Annual job":
	msg="choose the site"
	choices=["roberthalf","betterteam","indeed","timesjob"]
	choice=choicebox(msg,title,choices)
	if choice=="roberthalf":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://www.roberthalf.com/")
	elif choice=="betterteam":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://www.betterteam.com/")
	elif choice=="indeed":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://www.indeed.jobs/")
	elif choice=="timesjob":
		chromedriver="C:\\Users\\admin\\chromedriver"
		driver =webdriver.Chrome(chromedriver)
		driver.get("https://www.timesjobs.com/")
else:
	sys.exit(0)
		
