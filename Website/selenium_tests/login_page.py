# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING

def login_form_test(driver): 

	print("Testing login form.")
	print("WARNING: This code is intended only to show sample functionality.")
	print("WARNING: As such the plain text email and password here are only temporary credentials for development.")

	print("Testing correct login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("foo@bar.tld")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("secret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login worked correctly.")
	# logout
	print("Testing logout.")
	driver.get(PATH_STRING+"/logout")
	input("Press enter if logout worked correctly.")
	# attempting to access protected content after logout
	print("Attempting to access protected content after logout.")
	driver.get(PATH_STRING+"/protected")
	input("Press enter if access fails.")
	# return to the login page
	driver.get(PATH_STRING+"/login")

	# incorrect email, correct password
	print("Testing incorrect login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("fizz@bang.buzz")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("secret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login fails.")
	
	# correct email, correct password
	print("Testing incorrect login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("foo@bar.tld")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("fakesecret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login fails.")

	# incorrect email, incorrect password
	print("Testing incorrect login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("boom@bang.ouch")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("fakesecret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login fails.")

	print("Login test complete.")

def main():
	run_tests(login_form_test,PATH_STRING+"/login")

if __name__ == "__main__":
	main()
