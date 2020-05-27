import time
from selenium import webdriver
from selenium.webdriver.common.by import By									# Target enement to find if present
from selenium.webdriver.support.ui import WebDriverWait						# Wait for things
from selenium.webdriver.support import expected_conditions as EC			# Determine expectant conditions
from selenium.common.exceptions import TimeoutException						# Tell if something times out
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup												# Parse returned html data
from urllib.parse import urlparse											# Web scraping to find answer to question
import sys


# Get data, scraper prints out source
class Fetcher:
	def __init__(self, url):												# Init driver call method to look at data and return
		options = Options()
		options.add_argument('--headless')

		self.driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe', 
								 chrome_options=options)					# Browser
		self.driver.wait = WebDriverWait(self.driver, 5)					# Wait time 5 sec
		self.url = url														# Instance variable dont have to call


	def lookup(self):
		self.driver.get(self.url)
		try:												
			ip = self.driver.wait.until(EC.presence_of_element_located(
				(By.CLASS_NAME, "gsfi")
				))
		except:
			print("Failed")

		soup = BeautifulSoup(self.driver.page_source, "html.parser")		# Page returned, create beautiful soup from this
		answer = soup.find_all(class_= "kp-rgc")							# Look for answer in class on google page, try other clases

		if not answer:
			answer = soup.find_all(class_= "FLP8od")

		if not answer:
			answer = soup.find_all(class_= "e24Kjd")

		if not answer:
			answer = soup.find_all(class_= "di3YZe")

		if not answer:
			answer = "I can't find the answer."

		self.driver.quit()
		return answer[0].get_text()
		
